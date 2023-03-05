from rest_framework import serializers

from context.models.identifier_types import IdentifierTypes


class IdentifierTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifierTypes
        fields = '__all__'
