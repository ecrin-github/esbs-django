from rest_framework import serializers

from context.models.rms_user_types import RmsUserTypes


class RmsUserTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsUserTypes
        fields = '__all__'


class RmsUserTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsUserTypes
        fields = '__all__'
