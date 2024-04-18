from rest_framework import serializers

from context.models.legal_status_types import LegalStatusTypes


class LegalStatusTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalStatusTypes
        fields = '__all__'


class LegalStatusTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalStatusTypes
        fields = '__all__'
