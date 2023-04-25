from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from rms.models.dup.duas import DataUseAccesses
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses
from rms.serializers.dup.duas_dto import DataUseAccessesOutputSerializer
from rms.serializers.dup.dup_notes_dto import DupNotesOutputSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsOutputSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer
from rms.serializers.dup.dup_prereqs_dto import DupPrereqsOutputSerializer
from rms.serializers.dup.dup_secondary_use_dto import DupSecondaryUseOutputSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesOutputSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesOutputSerializer


class DataUseAccessesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseAccesses.objects.all()
    serializer_class = DataUseAccessesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataUseAccesses.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupNotesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupNotes.objects.all()
    serializer_class = DupNotesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupNotes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupObjectsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupObjects.objects.all()
    serializer_class = DupObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupObjects.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPeopleList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupPeople.objects.all()
    serializer_class = DupPeopleOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupPeople.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPrereqsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupPrereqs.objects.all()
    serializer_class = DupPrereqsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupPrereqs.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupSecondaryUseList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupSecondaryUse.objects.all()
    serializer_class = DupSecondaryUseOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupSecondaryUse.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupStudiesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupStudies.objects.all()
    serializer_class = DupStudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupStudies.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DataUseProcessesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseProcesses.objects.all()
    serializer_class = DataUseProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
