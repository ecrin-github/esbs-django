from rest_framework import serializers

from context.models.org_names_qualifier_types import OrgNameQualifierTypes


class OrgNameQualifierTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgNameQualifierTypes
        fields = '__all__'


class OrgNameQualifierTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgNameQualifierTypes
        fields = '__all__'
