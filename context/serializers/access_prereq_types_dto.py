from rest_framework import serializers

from context.models.access_prereq_types import AccessPrereqTypes


class AccessPrereqTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPrereqTypes
        fields = '__all__'


class AccessPrereqTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPrereqTypes
        fields = '__all__'
