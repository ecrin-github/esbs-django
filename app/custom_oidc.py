from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from django.core.exceptions import ImproperlyConfigured, SuspiciousOperation
from rest_framework import authentication, exceptions
from requests.exceptions import HTTPError
from mozilla_django_oidc.utils import import_from_settings, parse_www_authenticate_header


class CustomAuthenticationBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        """ Overrides Authentication Backend so that Django users are
            created with the keycloak preferred_username.
            If nothing found matching the email, then try the username.
        """
        user = super(CustomAuthenticationBackend, self).create_user(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.username = claims.get('email')
        user.save()
        return user

    def filter_users_by_claims(self, claims):
        """ Return all users matching the specified email.
            If nothing found matching the email, then try the username
        """
        email = claims.get('email')
        preferred_username = claims.get('email')

        if not email:
            return self.UserModel.objects.none()
        users = self.UserModel.objects.filter(email__iexact=email)

        if len(users) < 1:
            if not preferred_username:
                return self.UserModel.objects.none()
            users = self.UserModel.objects.filter(username__iexact=preferred_username)
        return users

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.username = claims.get('email')
        user.save()
        return user


class CustomAuthentication(OIDCAuthentication):
    def authenticate(self, request):
        """
        Authenticate the request and return a tuple of (user, token) or None
        if there was no authentication attempt.
        """
        access_token = self.get_access_token(request)

        if not access_token:
            return None

        try:
            user = self.backend.get_or_create_user(access_token, None, None)
        except HTTPError as exc:
            resp = exc.response

            # if the oidc provider returns 401, it means the token is invalid.
            # in that case, we want to return the upstream error message (which
            # we can get from the www-authentication header) in the response.
            if resp.status_code == 401 and 'www-authenticate' in resp.headers:
                data = parse_www_authenticate_header(resp.headers['www-authenticate'])
                if 'error_description' in data:
                    raise exceptions.AuthenticationFailed(data['error_description'])
                #AADB2C customization
                elif 'Bearer error' in data:
                    raise exceptions.AuthenticationFailed(data['Bearer error'])

            # for all other http errors, just re-raise the exception.
            raise
        except SuspiciousOperation as exc:
            #LOGGER.info('Login failed: %s', exc)
            raise exceptions.AuthenticationFailed('Login failed')

        if not user:
            msg = 'Login failed: No user found for the given access token.'
            raise exceptions.AuthenticationFailed(msg)

        return user, access_token