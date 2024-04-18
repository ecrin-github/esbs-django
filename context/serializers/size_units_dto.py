from rest_framework import serializers

from context.models.size_units import SizeUnits


class SizeUnitsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeUnits
        fields = '__all__'


class SizeUnitsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeUnits
        fields = '__all__'
