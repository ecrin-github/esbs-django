from django.db.models import Q
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import WriteOnlyForOwnOrg, IsSuperUser, ReadOnly
from mdm.views.common.mixins import MultipleFieldLookupMixin
from rms.models import DtpObjects
from mdm.models.study.studies import Studies
from mdm.models.study.study_contributors import StudyContributors
from mdm.models.study.study_features import StudyFeatures
from mdm.models.study.study_identifiers import StudyIdentifiers
from mdm.models.study.study_relationships import StudyRelationships
from mdm.models.study.study_titles import StudyTitles
from mdm.models.study.study_topics import StudyTopics
from mdm.models.study.study_number_sequence import StudyNumberSeq
from mdm.serializers.study.studies_dto import StudiesOutputSerializer, StudiesLimitedOutputSerializer, \
    StudiesInputSerializerCreate, StudiesInputSerializerUpdate
from mdm.serializers.study.study_contributors_dto import StudyContributorsOutputSerializer, \
    StudyContributorsLimitedOutputSerializer, StudyContributorsInputSerializer
from mdm.serializers.study.study_features_dto import StudyFeaturesOutputSerializer, StudyFeaturesInputSerializer
from mdm.serializers.study.study_identifiers_dto import StudyIdentifiersOutputSerializer, \
    StudyIdentifiersInputSerializer
from mdm.serializers.study.study_relationships_dto import StudyRelationshipsOutputSerializer, \
    StudyRelationshipsInputSerializer
from mdm.serializers.study.study_titles_dto import StudyTitlesOutputSerializer, StudyTitlesInputSerializer
from mdm.serializers.study.study_topics_dto import StudyTopicsOutputSerializer, StudyTopicsInputSerializer


class StudiesList(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Studies.objects.all()
    serializer_class = StudiesLimitedOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]
    lookup_fields = ['pk', 'sd_sid']

    def list(self, request):
        """ Not returning person field in study contributors if no org/study not from same org """
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
            queryset_full = Studies.objects.all()
        elif has_org:
            queryset_full = Studies.objects.filter(organisation=request.user.user_profile.organisation.id)
            queryset_limited = Studies.objects.filter(~Q(organisation=request.user.user_profile.organisation.id))
        else:
            queryset_limited = Studies.objects.all()
        
        if queryset_full is not None:
            serializer_full = StudiesOutputSerializer(queryset_full, many=True)
            count += queryset_full.count()
        if queryset_limited is not None:
            serializer_limited = StudiesLimitedOutputSerializer(queryset_limited, many=True)
            count += queryset_limited.count()

        return Response({'count': count, 'results': list(serializer_full.data if serializer_full is not None else []) 
                                                    + list(serializer_limited.data if serializer_limited is not None else []), 'statusCode': status.HTTP_200_OK})

    def retrieve(self, request, **kwargs):
        """ Not returning person field in study contributors if no org/study not from same org """
        study = self.get_object()

        serializer = None
        try:
            if request.user.is_superuser or request.user.user_profile.organisation.id == study.organisation.id:
                serializer = StudiesOutputSerializer(study)
        except AttributeError:
            pass
        if serializer is None:
            serializer = StudiesLimitedOutputSerializer(study)
        
        augmented_serializer_data = dict(serializer.data)
        for linked_do in augmented_serializer_data["linked_objects"]:
            if linked_do["object_type"] is not None and linked_do["object_type"]["name"].lower() == "individual participant data":
                # Adding DO release date
                release_date = ""
                dtp_dos = DtpObjects.objects.filter(data_object=linked_do["id"])
                if dtp_dos.exists():
                    for dtp_do in dtp_dos:
                        linked_do["test1"] = "yes"
                        if dtp_do.dtp_id.upload_complete_date:
                            release_date = dtp_do.dtp_id.upload_complete_date
                            break
                linked_do["release_date"] = release_date
                augmented_serializer_data["linked_objects"]

        return Response(augmented_serializer_data)

    def get_serializer_class(self):
        if self.action in ["create"]:
            return StudiesInputSerializerCreate
        elif self.action in ["update", "partial_update"]:
            return StudiesInputSerializerUpdate
        return super().get_serializer_class()


class StudyNextId(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & ReadOnly]

    def get(self, request, format=None):
        # Get next id, incremented after every insert in the DB
        order_number = StudyNumberSeq.objects.raw("select 1 as id, last_value from study_number_seq")[0].last_value
        next_id = f'DSRS-{order_number}'

        return Response({'sdSid': next_id})


class StudyContributorsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyContributors.objects.all()
    serializer_class = StudyContributorsLimitedOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyContributorsInputSerializer
        elif self.action in ["list", "retrieve"]:
            study_check = Studies.objects.filter(id=self.kwargs['studyId'])
            if study_check.exists():
                study = Studies.objects.get(id=self.kwargs['studyId'])
                try:
                    if self.request.user.is_superuser or self.request.user.user_profile.organisation.id == study.organisation.id:
                        return StudyContributorsOutputSerializer
                except AttributeError:
                    pass
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyContributors.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyFeaturesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyFeatures.objects.all()
    serializer_class = StudyFeaturesOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyFeaturesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyFeatures.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyIdentifiersList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyIdentifiers.objects.all()
    serializer_class = StudyIdentifiersOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyIdentifiersInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyIdentifiers.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyRelationshipsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyRelationships.objects.all()
    serializer_class = StudyRelationshipsOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyRelationshipsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyTitlesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyTitles.objects.all()
    serializer_class = StudyTitlesOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyTitlesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyTitles.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyTopicsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyTopics.objects.all()
    serializer_class = StudyTopicsOutputSerializer
    permission_classes = [IsSuperUser | WriteOnlyForOwnOrg | ReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyTopicsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyTopics.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )
