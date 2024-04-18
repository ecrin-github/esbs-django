from rest_framework import serializers

from context.serializers.org_relationship_types_dto import OrgRelationshipTypesOutputSerializer
from general.models.org_relationships import OrgRelationships
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgRelationshipsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRelationships
        fields = '__all__'


class OrgRelationshipsOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    relationship_type = OrgRelationshipTypesOutputSerializer(many=False, read_only=True)
    target_org = OrganisationsOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgRelationships
        fields = '__all__'
