from rest_framework import serializers

from context.serializers.geog_entity_types_dto import GeogEntityTypesOutputSerializer
from general.models.geog_entities import GeogEntities


class GeogEntitiesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeogEntities
        fields = '__all__'


class GeogEntitiesOutputSerializer(serializers.ModelSerializer):
    geog_entity_type = GeogEntityTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = GeogEntities
        fields = '__all__'
