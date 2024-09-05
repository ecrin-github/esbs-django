from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
import json
import jwt
import requests

from configs.identity_configs import PUBLIC_KEY_ENDPOINT
from users.models import UserProfiles


class JWTAuthMiddleware(BaseMiddleware):
    """
    LS AAI JWT token authentication middleware
    https://medium.com/@josephmiracle119/authentication-in-websocket-with-django-and-django-rest-framework-drf-50406ef95f3c#7266
    """
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        token = self.get_token_from_scope(scope)
        
        if token != None:
            user_id = await self.get_user_from_token(token) 
            if user_id:
                scope['token'] = token
                scope['user_id'] = user_id
            else:
                scope['error'] = 'Invalid token'

        if token == None:
            scope['error'] = 'Please provide an auth token'
                
        return await super().__call__(scope, receive, send)

    def get_token_from_scope(self, scope):
        headers = dict(scope.get("headers", {}))
        ws_header = headers.get(b'sec-websocket-protocol', b'').decode('utf-8')
        return ws_header
        
    @database_sync_to_async
    def get_user_from_token(self, token):
        try:
            # Verifying LS AAI JWT Token with their public key - https://renzolucioni.com/verifying-jwts-with-jwks-and-pyjwt/
            jwks = json.loads(requests.get(PUBLIC_KEY_ENDPOINT).text)
            public_keys = {}
            for jwk in jwks['keys']:
                kid = jwk['kid']
                public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

            kid = jwt.get_unverified_header(token)['kid']
            key = public_keys[kid]

            access_token = jwt.decode(token, key=key, algorithms="RS256", options={"verify_aud": False, "verify_signature": True},)
            
            user_check = UserProfiles.objects.filter(ls_aai_id=access_token['sub'])
            if user_check.exists():
                return UserProfiles.objects.get(ls_aai_id=access_token['sub']).user_id
        except Exception as e:
            pass
        return None