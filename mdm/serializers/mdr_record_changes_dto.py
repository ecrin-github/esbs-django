from rest_framework import serializers

from mdm.models.mdr_record_changes import MdrRecordChanges


class MdrRecordChangesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdrRecordChanges
        fields = '__all__'


class MdrRecordChangesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdrRecordChanges
        fields = '__all__'
