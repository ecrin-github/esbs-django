from rest_framework import serializers

from context.models.org_link_types import OrgLinkTypes


class OrgLinkTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLinkTypes
        fields = '__all__'


class OrgLinkTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLinkTypes
        fields = '__all__'
