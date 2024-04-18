from rest_framework import serializers

from context.serializers.org_link_types_dto import OrgLinkTypesOutputSerializer
from general.models.org_links import OrgLinks
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgLinksInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLinks
        fields = '__all__'


class OrgLinksOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    org_link_type = OrgLinkTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgLinks
        fields = '__all__'
