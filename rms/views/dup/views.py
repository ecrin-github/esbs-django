from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from app.permissions import ReadOnly, ReadOnlyForOwnOrg, IsSuperUser
from rms.models.dup.duas import DataUseAccesses
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses
from rms.serializers.dup.duas_dto import DataUseAccessesOutputSerializer, DataUseAccessesInputSerializer
from rms.serializers.dup.dup_notes_dto import DupNotesOutputSerializer, DupNotesInputSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsOutputSerializer, DupObjectsInputSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer, DupPeopleInputSerializer
from rms.serializers.dup.dup_secondary_use_dto import DupSecondaryUseOutputSerializer, DupSecondaryUseInputSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesOutputSerializer, DupStudiesInputSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesOutputSerializer, DataUseProcessesInputSerializer


class DataUseAccessesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseAccesses.objects.all()
    serializer_class = DataUseAccessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseAccessesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataUseAccesses.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupNotesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupNotes.objects.all()
    serializer_class = DupNotesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupNotesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupNotes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupObjectsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupObjects.objects.all()
    serializer_class = DupObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupObjectsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupObjects.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPeopleList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupPeople.objects.all()
    serializer_class = DupPeopleOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupPeopleInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupPeople.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupSecondaryUseList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupSecondaryUse.objects.all()
    serializer_class = DupSecondaryUseOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupSecondaryUseInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupSecondaryUse.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupStudiesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupStudies.objects.all()
    serializer_class = DupStudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupStudiesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupStudies.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DataUseProcessesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseProcesses.objects.all()
    serializer_class = DataUseProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseProcessesInputSerializer
        return super().get_serializer_class()
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return (
                super()
                .get_queryset(*args, **kwargs)
            )
        else:
            if user.user_profile and user.user_profile.organisation:
                organisation = user.user_profile.organisation.id
            else:
                organisation = None
            return (
                super()
                .get_queryset(*args, **kwargs)
                .filter(organisation=organisation)
            )
