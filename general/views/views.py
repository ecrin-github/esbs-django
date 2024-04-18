from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from general.models.geog_entities import GeogEntities
from general.models.language_codes import LanguageCodes
from general.models.mesh_lookup import MeshLookup
from general.models.org_attributes import OrgAttributes
from general.models.org_links import OrgLinks
from general.models.org_locations import OrgLocations
from general.models.org_names import OrgNames
from general.models.org_relationships import OrgRelationships
from general.models.org_type_membership import OrgTypeMembership
from general.models.organisations import Organisations
from general.models.published_journals import PublishedJournals
from general.serializers.geog_entities_dto import GeogEntitiesOutputSerializer
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from general.serializers.mesh_lookup_dto import MeshLookupOutputSerializer
from general.serializers.org_attributes_dto import OrgAttributesOutputSerializer
from general.serializers.org_links_dto import OrgLinksOutputSerializer
from general.serializers.org_locations_dto import OrgLocationsOutputSerializer
from general.serializers.org_names_dto import OrgNamesOutputSerializer
from general.serializers.org_relationships_dto import OrgRelationshipsOutputSerializer
from general.serializers.org_type_membership_dto import OrgTypeMembershipOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from general.serializers.published_journals_dto import PublishedJournalsOutputSerializer


# Create your views here.
class GeogEntitiesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = GeogEntities.objects.all()
    serializer_class = GeogEntitiesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MeshLookupList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = MeshLookup.objects.all()
    serializer_class = MeshLookupOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgAttributes.objects.all()
    serializer_class = OrgAttributesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgAttributes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgLinksList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgLinks.objects.all()
    serializer_class = OrgLinksOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgLinks.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgLocationsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgLocations.objects.all()
    serializer_class = OrgLocationsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgLocations.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgNamesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgNames.objects.all()
    serializer_class = OrgNamesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgNames.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgRelationshipsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgRelationships.objects.all()
    serializer_class = OrgRelationshipsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgTypeMembershipList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgTypeMembership.objects.all()
    serializer_class = OrgTypeMembershipOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgTypeMembership.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class PublishedJournalsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = PublishedJournals.objects.all()
    serializer_class = PublishedJournalsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageCodesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = LanguageCodes.objects.all()
    serializer_class = LanguageCodesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganisationsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Organisations.objects.all()
    serializer_class = OrganisationsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
