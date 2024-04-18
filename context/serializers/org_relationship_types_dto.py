from rest_framework import serializers

from context.models.org_relationship_types import OrgRelationshipTypes


class OrgRelationshipTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRelationshipTypes
        fields = '__all__'


class OrgRelationshipTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRelationshipTypes
        fields = '__all__'
