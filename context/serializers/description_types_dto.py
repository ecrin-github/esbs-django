from rest_framework import serializers

from context.models.description_types import DescriptionTypes


class DescriptionTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionTypes
        fields = '__all__'


class DescriptionTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionTypes
        fields = '__all__'
