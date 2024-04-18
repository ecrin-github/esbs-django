from rest_framework import serializers

from context.models.org_attribute_types import OrgAttributeTypes
from context.serializers.org_attribute_datatypes_dto import OrgAttributeDatatypesOutputSerializer


class OrgAttributeTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgAttributeTypes
        fields = '__all__'


class OrgAttributeTypesOutputSerializer(serializers.ModelSerializer):
    org_attribute_datatype = OrgAttributeDatatypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgAttributeTypes
        fields = '__all__'
