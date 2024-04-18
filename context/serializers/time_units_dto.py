from rest_framework import serializers

from context.models.time_units import TimeUnits


class TimeUnitsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnits
        fields = '__all__'


class TimeUnitsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnits
        fields = '__all__'
