from rest_framework import serializers

from context.models.object_filter_types import ObjectFilterTypes


class ObjectFilterTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectFilterTypes
        fields = '__all__'


class ObjectFilterTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectFilterTypes
        fields = '__all__'
