from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from rms.models.dup.dup_prereqs import DupPrereqs


class DupPrereqsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupPrereqs
        fields = '__all__'


class DupPrereqsOutputSerializer(serializers.ModelSerializer):
    prereq_type = AccessPrereqTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DupPrereqs
        fields = '__all__'
