from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesOutputSerializer
from rms.models.dtp.dtp_studies import DtpStudies
from users.serializers.users_dto import UsersSerializer


class DtpStudiesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpStudies
        fields = '__all__'


class DtpStudiesOutputSerializer(serializers.ModelSerializer):
    md_check_status = CheckStatusTypesOutputSerializer(many=False, read_only=True)
    md_check_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpStudies
        fields = '__all__'
