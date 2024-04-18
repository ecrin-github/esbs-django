from rest_framework import serializers

from context.models.check_status_types import CheckStatusTypes


class CheckStatusTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckStatusTypes
        fields = '__all__'


class CheckStatusTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckStatusTypes
        fields = '__all__'
