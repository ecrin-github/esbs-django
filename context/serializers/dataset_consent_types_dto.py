from rest_framework import serializers

from context.models.dataset_consent_types import DatasetConsentTypes


class DatasetConsentTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetConsentTypes
        fields = '__all__'


class DatasetConsentTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetConsentTypes
        fields = '__all__'
