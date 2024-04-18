from rest_framework import serializers

from context.models.resource_types import ResourceTypes


class ResourceTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTypes
        fields = '__all__'


class ResourceTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTypes
        fields = '__all__'
