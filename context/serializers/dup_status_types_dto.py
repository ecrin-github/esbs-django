from rest_framework import serializers

from context.models.dup_status_types import DupStatusTypes


class DupStatusTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStatusTypes
        fields = '__all__'


class DupStatusTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStatusTypes
        fields = '__all__'
