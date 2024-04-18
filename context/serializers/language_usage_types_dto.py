from rest_framework import serializers

from context.models.language_usage_types import LanguageUsageTypes


class LanguageUsageTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageUsageTypes
        fields = '__all__'


class LanguageUsageTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageUsageTypes
        fields = '__all__'
