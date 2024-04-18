from rest_framework import serializers

from context.models.object_instance_types import ObjectInstanceTypes


class ObjectInstanceTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectInstanceTypes
        fields = '__all__'


class ObjectInstanceTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectInstanceTypes
        fields = '__all__'
