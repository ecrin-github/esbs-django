from rest_framework import serializers

from context.models.doi_status_types import DoiStatusTypes


class DoiStatusTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoiStatusTypes
        fields = '__all__'


class DoiStatusTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoiStatusTypes
        fields = '__all__'
