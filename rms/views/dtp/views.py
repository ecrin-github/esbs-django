from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from app.permissions import ReadOnly, ReadOnlyForOwnOrg, IsSuperUser
from rms.models.dtp.dtas import DataTransferAccesses
from rms.models.dtp.dtp_datasets import DtpDatasets
from rms.models.dtp.dtp_notes import DtpNotes
from rms.models.dtp.dtp_objects import DtpObjects
from rms.models.dtp.dtp_people import DtpPeople
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.models.dtp.dtp_studies import DtpStudies
from rms.models.dtp.dtps import DataTransferProcesses
from rms.serializers.dtp.dtas_dto import DataTransferAccessesOutputSerializer, DataTransferAccessesInputSerializer
from rms.serializers.dtp.dtp_datasets_dto import DtpDatasetsOutputSerializer, DtpDatasetsInputSerializer
from rms.serializers.dtp.dtp_notes_dto import DtpNotesOutputSerializer, DtpNotesInputSerializer
from rms.serializers.dtp.dtp_objects_dto import DtpObjectsOutputSerializer, DtpObjectsInputSerializer
from rms.serializers.dtp.dtp_people_dto import DtpPeopleOutputSerializer, DtpPeopleInputSerializer
from rms.serializers.dtp.dtp_prereqs_dto import DtpPrereqsOutputSerializer, DtpPrereqsInputSerializer
from rms.serializers.dtp.dtp_studies_dto import DtpStudiesOutputSerializer, DtpStudiesInputSerializer
from rms.serializers.dtp.dtps_dto import DataTransferProcessesOutputSerializer, \
    DataTransferProcessesDetailsOutputSerializer, DataTransferProcessesInputSerializer


class DataTransferAccessesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataTransferAccesses.objects.all()
    serializer_class = DataTransferAccessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataTransferAccessesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataTransferAccesses.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpDatasetsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpDatasets.objects.all()
    serializer_class = DtpDatasetsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpDatasetsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpDatasets.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpNotesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpNotes.objects.all()
    serializer_class = DtpNotesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpNotesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpNotes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpObjectsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpObjects.objects.all()
    serializer_class = DtpObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpObjectsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpObjects.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpPeopleList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpPeople.objects.all()
    serializer_class = DtpPeopleOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpPeopleInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpPeople.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpPrereqsList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpPrereqs.objects.all()
    serializer_class = DtpPrereqsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpPrereqsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpPrereqs.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpStudiesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpStudies.objects.all()
    serializer_class = DtpStudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnlyForOwnOrg)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DtpStudiesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpStudies.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DataTransferProcessesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataTransferProcesses.objects.all()
    serializer_class = DataTransferProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataTransferProcessesInputSerializer
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
