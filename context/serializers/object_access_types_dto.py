from rest_framework import serializers

from context.models.object_access_types import ObjectAccessTypes


class ObjectAccessTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectAccessTypes
        fields = '__all__'


class ObjectAccessTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectAccessTypes
        fields = '__all__'
