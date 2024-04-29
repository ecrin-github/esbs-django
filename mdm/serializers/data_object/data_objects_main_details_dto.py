from rest_framework import serializers

from mdm.models.data_object.data_objects import DataObjects


class ObjectMainDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataObjects
        fields = ['id', 'sd_oid', 'display_title', 'doi']