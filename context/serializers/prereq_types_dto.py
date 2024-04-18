from rest_framework import serializers

from context.models.prereq_types import PrereqTypes


class PrereqTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrereqTypes
        fields = '__all__'


class PrereqTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrereqTypes
        fields = '__all__'
