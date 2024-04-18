from rest_framework import serializers

from context.serializers.org_types_dto import OrgTypesOutputSerializer
from general.models.org_type_membership import OrgTypeMembership
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgTypeMembershipInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgTypeMembership
        fields = '__all__'


class OrgTypeMembershipOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    org_type = OrgTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgTypeMembership
        fields = '__all__'
