from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesOutputSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesOutputSerializer
from rms.models.dtp.dtp_objects import DtpObjects
from users.serializers.users_dto import UsersSerializer


class DtpObjectsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpObjects
        fields = '__all__'


class DtpObjectsOutputSerializer(serializers.ModelSerializer):
    access_type = ObjectAccessTypesOutputSerializer(many=False, read_only=True)
    access_check_status = CheckStatusTypesOutputSerializer(many=False, read_only=True)
    access_check_by = UsersSerializer(many=False, read_only=True)
    md_check_status = CheckStatusTypesOutputSerializer(many=False, read_only=True)
    md_check_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpObjects
        fields = '__all__'
