from rest_framework import serializers

from context.serializers.dup_status_types_dto import DupStatusTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from rms.models.dup.dups import DataUseProcesses


class DataUseProcessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseProcesses
        fields = '__all__'


class DataUseProcessesOutputSerializer(serializers.ModelSerializer):
    status = DupStatusTypesOutputSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataUseProcesses
        fields = '__all__'
