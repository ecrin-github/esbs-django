from rest_framework import serializers

from context.models.geog_entity_types import GeogEntityTypes


class GeogEntityTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeogEntityTypes
        fields = '__all__'


class GeogEntityTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeogEntityTypes
        fields = '__all__'
