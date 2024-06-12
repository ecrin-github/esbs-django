from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.serializers.dtp.dtp_objects_dto import DtpObjectsOutputSerializer
from mdm.serializers.data_object.data_objects_main_details_dto import ObjectMainDetailsSerializer


class DtpPrereqsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpPrereqs
        fields = '__all__'


class DtpPrereqsOutputSerializer(serializers.ModelSerializer):
    prereq_type = AccessPrereqTypesOutputSerializer(many=False, read_only=True)
    dtp_data_object = DtpObjectsOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DtpPrereqs
        fields = '__all__'
