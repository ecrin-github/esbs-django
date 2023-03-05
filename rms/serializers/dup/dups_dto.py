from rest_framework import serializers

from context.serializers.dup_status_types_dto import DupStatusTypesSerializer
from rms.models.dup.dups import DataUseProcesses


class DataUseProcessesSerializer(serializers.ModelSerializer):
    status = DupStatusTypesSerializer(many=False, read_only=True)

    class Meta:
        model = DataUseProcesses
        fields = '__all__'
