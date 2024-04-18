from rest_framework import serializers

from context.models.object_classes import ObjectClasses


class ObjectClassesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectClasses
        fields = '__all__'


class ObjectClassesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectClasses
        fields = '__all__'
