from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from app.permissions import ReadOnly, IsSuperUser
from mdm.views.common.mixins import GetAuthFilteringMixin
from rms.models.dup.duas import DataUseAgreements
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses
from rms.serializers.dup.duas_dto import DataUseAgreementsOutputSerializer, DataUseAgreementsInputSerializer
from rms.serializers.dup.dup_notes_dto import DupNotesOutputSerializer, DupNotesInputSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsOutputSerializer, DupObjectsInputSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer, DupPeopleInputSerializer
from rms.serializers.dup.dup_secondary_use_dto import DupSecondaryUseOutputSerializer, DupSecondaryUseInputSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesOutputSerializer, DupStudiesInputSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesOutputSerializer, DataUseProcessesInputSerializer


class DataUseAgreementsList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseAgreements.objects.all()
    object_class = DataUseAgreements
    serializer_class = DataUseAgreementsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseAgreementsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        # TODO (for multiple views): return unauthorised error if trying to get DUAs for a unauthorised DUP instead of empty result set
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupNotesList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupNotes.objects.all()
    object_class = DupNotes
    serializer_class = DupNotesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupNotesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupObjectsList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupObjects.objects.all()
    object_class = DupObjects
    serializer_class = DupObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupObjectsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPeopleList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupPeople.objects.all()
    object_class = DupPeople
    serializer_class = DupPeopleOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupPeopleInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupSecondaryUseList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupSecondaryUse.objects.all()
    obejct_class = DupSecondaryUse
    serializer_class = DupSecondaryUseOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupSecondaryUseInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupStudiesList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupStudies.objects.all()
    object_class = DupStudies
    serializer_class = DupStudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupStudiesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DataUseProcessesList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseProcesses.objects.all()
    object_class = DataUseProcesses
    serializer_class = DataUseProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseProcessesInputSerializer
        return super().get_serializer_class()
