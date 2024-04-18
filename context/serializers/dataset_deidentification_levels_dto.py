from rest_framework import serializers

from context.models.dataset_deidentification_levels import DatasetDeidentificationLevels


class DatasetDeidentificationLevelsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetDeidentificationLevels
        fields = '__all__'


class DatasetDeidentificationLevelsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetDeidentificationLevels
        fields = '__all__'
