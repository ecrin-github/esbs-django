from rest_framework import serializers

from rms.models.rms_record_changes import RmsRecordChanges


class RmsRecordChangesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsRecordChanges
        fields = '__all__'


class RmsRecordChangesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsRecordChanges
        fields = '__all__'
