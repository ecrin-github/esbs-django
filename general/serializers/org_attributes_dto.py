from rest_framework import serializers

from context.serializers.org_attribute_types_dto import OrgAttributeTypesOutputSerializer
from general.models.org_attributes import OrgAttributes
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgAttributesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgAttributes
        fields = '__all__'


class OrgAttributesOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    attribute_type = OrgAttributeTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgAttributes
        fields = '__all__'
