from rest_framework import serializers

from context.models.title_types import TitleTypes


class TitleTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleTypes
        fields = '__all__'


class TitleTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleTypes
        fields = '__all__'
