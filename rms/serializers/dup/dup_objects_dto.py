from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from rms.models.dup.dup_objects import DupObjects
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer


class DupObjectsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupObjects
        fields = '__all__'


class DupObjectsOutputSerializer(serializers.ModelSerializer):
    access_type = AccessPrereqTypesOutputSerializer(many=False, read_only=True)
    data_object = DataObjectsOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DupObjects
        fields = '__all__'
