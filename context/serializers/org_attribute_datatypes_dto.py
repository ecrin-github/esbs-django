from rest_framework import serializers

from context.models.org_attribute_datatypes import OrgAttributeDatatypes


class OrgAttributeDatatypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgAttributeDatatypes
        fields = '__all__'


class OrgAttributeDatatypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgAttributeDatatypes
        fields = '__all__'
