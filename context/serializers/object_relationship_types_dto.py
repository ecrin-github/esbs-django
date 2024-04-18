from rest_framework import serializers

from context.models.object_relationship_types import ObjectRelationshipTypes


class ObjectRelationshipTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectRelationshipTypes
        fields = '__all__'


class ObjectRelationshipTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectRelationshipTypes
        fields = '__all__'
