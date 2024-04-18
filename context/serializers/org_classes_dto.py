from rest_framework import serializers

from context.models.org_classes import OrgClasses


class OrgClassesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgClasses
        fields = '__all__'


class OrgClassesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgClasses
        fields = '__all__'
