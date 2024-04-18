from rest_framework import serializers

from context.models.object_types import ObjectTypes
from context.serializers.object_classes_dto import ObjectClassesOutputSerializer
from context.serializers.object_filter_types_dto import ObjectFilterTypesOutputSerializer


class ObjectTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectTypes
        fields = '__all__'


class ObjectTypesOutputSerializer(serializers.ModelSerializer):
    filter_as = ObjectFilterTypesOutputSerializer(many=False, read_only=True)
    object_class = ObjectClassesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTypes
        fields = '__all__'
