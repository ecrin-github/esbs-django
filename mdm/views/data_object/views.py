from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from mdm.models.data_object.data_objects import DataObjects
from mdm.models.data_object.object_contributors import ObjectContributors
from mdm.models.data_object.object_datasets import ObjectDatasets
from mdm.models.data_object.object_dates import ObjectDates
from mdm.models.data_object.object_descriptions import ObjectDescriptions
from mdm.models.data_object.object_identifiers import ObjectIdentifiers
from mdm.models.data_object.object_instances import ObjectInstances
from mdm.models.data_object.object_relationships import ObjectRelationships
from mdm.models.data_object.object_rights import ObjectRights
from mdm.models.data_object.object_titles import ObjectTitles
from mdm.models.data_object.object_topics import ObjectTopics
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer, DataObjectsInputSerializer
from mdm.serializers.data_object.object_contributors_dto import ObjectContributorsOutputSerializer, \
    ObjectContributorsInputSerializer
from mdm.serializers.data_object.object_datasets_dto import ObjectDatasetsOutputSerializer, \
    ObjectDatasetsInputSerializer
from mdm.serializers.data_object.object_dates_dto import ObjectDatesOutputSerializer, ObjectDatesInputSerializer
from mdm.serializers.data_object.object_descriptions_dto import ObjectDescriptionsOutputSerializer, \
    ObjectDescriptionsInputSerializer
from mdm.serializers.data_object.object_identifiers_dto import ObjectIdentifiersOutputSerializer, \
    ObjectIdentifiersInputSerializer
from mdm.serializers.data_object.object_instances_dto import ObjectInstancesOutputSerializer, \
    ObjectInstancesInputSerializer
from mdm.serializers.data_object.object_relationships_dto import ObjectRelationshipsOutputSerializer, \
    ObjectRelationshipsInputSerializer
from mdm.serializers.data_object.object_rights_dto import ObjectRightsOutputSerializer, ObjectRightsInputSerializer
from mdm.serializers.data_object.object_titles_dto import ObjectTitlesOutputSerializer, ObjectTitlesInputSerializer
from mdm.serializers.data_object.object_topics_dto import ObjectTopicsOutputSerializer, ObjectTopicsInputSerializer


class DataObjectsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataObjects.objects.all()
    serializer_class = DataObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataObjectsInputSerializer
        return super().get_serializer_class()


class ObjectContributorsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectContributors.objects.all()
    serializer_class = ObjectContributorsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectContributorsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectContributors.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDatasetsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectDatasets.objects.all()
    serializer_class = ObjectDatasetsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectDatasetsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDatasets.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDatesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectDates.objects.all()
    serializer_class = ObjectDatesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectDatesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDates.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDescriptionsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectDescriptions.objects.all()
    serializer_class = ObjectDescriptionsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectDescriptionsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDescriptions.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectIdentifiersList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectIdentifiers.objects.all()
    serializer_class = ObjectIdentifiersOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectIdentifiersInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectIdentifiers.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectInstancesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectInstances.objects.all()
    serializer_class = ObjectInstancesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectInstancesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectInstances.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectRelationshipsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectRelationships.objects.all()
    serializer_class = ObjectRelationshipsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectRelationshipsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectRightsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectRights.objects.all()
    serializer_class = ObjectRightsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectRightsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectRights.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectTitlesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectTitles.objects.all()
    serializer_class = ObjectTitlesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectTitlesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectTitles.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectTopicsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectTopics.objects.all()
    serializer_class = ObjectTopicsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectTopicsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectTopics.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )
