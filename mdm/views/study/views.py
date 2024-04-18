from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from mdm.models.study.studies import Studies
from mdm.models.study.study_contributors import StudyContributors
from mdm.models.study.study_features import StudyFeatures
from mdm.models.study.study_identifiers import StudyIdentifiers
from mdm.models.study.study_relationships import StudyRelationships
from mdm.models.study.study_titles import StudyTitles
from mdm.models.study.study_topics import StudyTopics
from mdm.serializers.study.studies_dto import StudiesOutputSerializer, StudiesInputSerializer
from mdm.serializers.study.study_contributors_dto import StudyContributorsOutputSerializer, \
    StudyContributorsInputSerializer
from mdm.serializers.study.study_features_dto import StudyFeaturesOutputSerializer, StudyFeaturesInputSerializer
from mdm.serializers.study.study_identifiers_dto import StudyIdentifiersOutputSerializer, \
    StudyIdentifiersInputSerializer
from mdm.serializers.study.study_relationships_dto import StudyRelationshipsOutputSerializer, \
    StudyRelationshipsInputSerializer
from mdm.serializers.study.study_titles_dto import StudyTitlesOutputSerializer, StudyTitlesInputSerializer
from mdm.serializers.study.study_topics_dto import StudyTopicsOutputSerializer, StudyTopicsInputSerializer


class StudiesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Studies.objects.all()
    serializer_class = StudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudiesInputSerializer
        return super().get_serializer_class()


class StudyContributorsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyContributors.objects.all()
    serializer_class = StudyContributorsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudyContributorsInputSerializer
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
