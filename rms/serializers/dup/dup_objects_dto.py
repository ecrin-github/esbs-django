from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from rms.models.dup.dup_objects import DupObjects


class DupObjectsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupObjects
        fields = '__all__'


class DupObjectsOutputSerializer(serializers.ModelSerializer):
    access_type = AccessPrereqTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DupObjects
        fields = '__all__'
