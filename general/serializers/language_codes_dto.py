from rest_framework import serializers

from general.models.language_codes import LanguageCodes


class LanguageCodesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCodes
        fields = '__all__'


class LanguageCodesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCodes
        fields = '__all__'
