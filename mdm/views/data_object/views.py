from django.db.models import Q
from django.shortcuts import get_object_or_404
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import WriteOnlyForOwnOrg, IsSuperUser, ReadOnly
from mdm.views.common.mixins import MultipleFieldLookupMixin, ParentMultipleFieldLookupMixin
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
from mdm.models.data_object.object_number_sequence import ObjectNumberSeq
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer, DataObjectsLimitedOutputSerializer, \
    DataObjectsInputSerializerCreate, DataObjectsInputSerializerUpdate
from mdm.serializers.data_object.object_contributors_dto import ObjectContributorsOutputSerializer, \
    ObjectContributorsLimitedOutputSerializer, ObjectContributorsInputSerializer
from mdm.serializers.data_object.object_datasets_dto import ObjectDatasetsOutputSerializer, \
    ObjectDatasetsInputSerializer
from mdm.serializers.data_object.object_dates_dto import ObjectDatesOutputSerializer, ObjectDatesInputSerializer
from mdm.serializers.data_object.object_descriptions_dto import ObjectDescriptionsOutputSerializer, \
    ObjectDescriptionsInputSerializer
from mdm.serializers.data_object.object_identifiers_dto import ObjectIdentifiersOutputSerializer, \
    ObjectIdentifiersInputSerializer
from mdm.serializers.data_object.object_instances_dto import ObjectInstancesOutputSerializer, \
    ObjectInstancesInputSerializerCreate, ObjectInstancesInputSerializerUpdate
from mdm.serializers.data_object.object_relationships_dto import ObjectRelationshipsOutputSerializer, \
    ObjectRelationshipsInputSerializer
from mdm.serializers.data_object.object_rights_dto import ObjectRightsOutputSerializer, ObjectRightsInputSerializer
from mdm.serializers.data_object.object_titles_dto import ObjectTitlesOutputSerializer, ObjectTitlesInputSerializer
from mdm.serializers.data_object.object_topics_dto import ObjectTopicsOutputSerializer, ObjectTopicsInputSerializer


class DataObjectsList(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataObjects.objects.all()
    serializer_class = DataObjectsLimitedOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]
    lookup_fields = ['pk', 'sd_oid']

    def list(self, request):
        """ Not returning person field in object contributors if no org/DO not from same org """
        queryset_full = None
        queryset_limited = None
        serializer_full = None
        serializer_limited = None
        has_org = False
        is_superuser = False
        count = 0

        try:
            if request.user.is_superuser:
                is_superuser = True
            if request.user.user_profile.organisation.id:
                has_org = True
        except AttributeError:
            pass

        if is_superuser:
            queryset_full = DataObjects.objects.all()
        elif has_org:
            queryset_full = DataObjects.objects.filter(organisation=request.user.user_profile.organisation.id)
            queryset_limited = DataObjects.objects.filter(~Q(organisation=request.user.user_profile.organisation.id))
        else:
            queryset_limited = DataObjects.objects.all()
        
        if queryset_full is not None:
            serializer_full = DataObjectsOutputSerializer(queryset_full, many=True)
            count += queryset_full.count()
        if queryset_limited is not None:
            serializer_limited = DataObjectsLimitedOutputSerializer(queryset_limited, many=True)
            count += queryset_limited.count()
        
        return Response({'count': count, 'results': list(serializer_full.data if serializer_full is not None else []) 
                                                    + list(serializer_limited.data if serializer_limited is not None else []), 'statusCode': status.HTTP_200_OK})

    def retrieve(self, request, **kwargs):
        """ Not returning person field in object contributors if no org/DO not from same org """
        data_object = self.get_object()

        serializer = None
        try:
            if request.user.is_superuser or request.user.user_profile.organisation.id == data_object.organisation.id:
                serializer = DataObjectsOutputSerializer(data_object)
        except AttributeError:
            pass
        if serializer is None:
            serializer = DataObjectsLimitedOutputSerializer(data_object)

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ["create"]:
            return DataObjectsInputSerializerCreate
        elif self.action in ["update", "partial_update"]:
            return DataObjectsInputSerializerUpdate
        return super().get_serializer_class()


class ObjectNextId(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & ReadOnly]

    def get(self, request, format=None):
        # Get next id, incremented after every insert in the DB
        order_number = ObjectNumberSeq.objects.raw("select 1 as id, last_value from object_number_seq")[0].last_value
        next_id = f'DSRO-{order_number}'

        return Response({'sdOid': next_id})


class ObjectContributorsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectContributors.objects.all()
    serializer_class = ObjectContributorsLimitedOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ObjectContributorsInputSerializer
        elif self.action in ["list", "retrieve"]:
            data_object_check = DataObjects.objects.filter(id=self.kwargs['objectId'])
            if data_object_check.exists():
                data_object = DataObjects.objects.get(id=self.kwargs['objectId'])
                try:
                    if self.request.user.is_superuser or self.request.user.user_profile.organisation.id == data_object.organisation.id:
                        return ObjectContributorsOutputSerializer
                except AttributeError:
                    pass
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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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


class ObjectInstancesList(ParentMultipleFieldLookupMixin, MultipleFieldLookupMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]
    serializer_class = ObjectInstancesOutputSerializer
    queryset = ObjectInstances.objects.all()
    object_class = ObjectInstances
    lookup_fields = ["pk", "sd_iid"]
    parent_lookup_fields = {
        "objectId": "id",
        "sd_oid": "sd_oid",
    }
    parent_queryset = DataObjects.objects.all()
    fk_lookup_field = "data_object"

    def get_serializer_class(self):
        if self.action in ["create"]:
            return ObjectInstancesInputSerializerCreate
        elif self.action in ["update", "partial_update"]:
            return ObjectInstancesInputSerializerUpdate
        return super().get_serializer_class()


class ObjectRelationshipsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectRelationships.objects.all()
    serializer_class = ObjectRelationshipsOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

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
