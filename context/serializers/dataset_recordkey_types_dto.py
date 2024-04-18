from rest_framework import serializers

from context.models.dataset_recordkey_types import DatasetRecordkeyTypes


class DatasetRecordkeyTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetRecordkeyTypes
        fields = '__all__'


class DatasetRecordkeyTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetRecordkeyTypes
        fields = '__all__'
