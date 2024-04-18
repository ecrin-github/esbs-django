from rest_framework import serializers

from context.serializers.dtp_status_types_dto import DtpStatusTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from rms.models.dtp.dtps import DataTransferProcesses


class DataTransferProcessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferProcesses
        fields = '__all__'


class DataTransferProcessesOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    status = DtpStatusTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferProcesses
        fields = '__all__'


class DataTransferProcessesDetailsOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    status = DtpStatusTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferProcesses
        fields = '__all__'
