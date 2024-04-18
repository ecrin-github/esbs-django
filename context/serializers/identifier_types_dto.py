from rest_framework import serializers

from context.models.identifier_types import IdentifierTypes


class IdentifierTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifierTypes
        fields = '__all__'


class IdentifierTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifierTypes
        fields = '__all__'
