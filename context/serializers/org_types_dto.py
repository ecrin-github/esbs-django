from rest_framework import serializers

from context.models.org_types import OrgTypes
from context.serializers.org_classes_dto import OrgClassesOutputSerializer


class OrgTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgTypes
        fields = '__all__'


class OrgTypesOutputSerializer(serializers.ModelSerializer):
    org_class = OrgClassesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgTypes
        fields = '__all__'
