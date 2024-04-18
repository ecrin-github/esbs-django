from rest_framework import serializers

from context.models.date_types import DateTypes


class DateTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTypes
        fields = '__all__'


class DateTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTypes
        fields = '__all__'
