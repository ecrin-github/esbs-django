from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesOutputSerializer
from mdm.serializers.study.study_main_details_dto import StudyMainDetailsSerializer
from rms.models.dtp.dtp_studies import DtpStudies
from users.serializers.users_dto import UsersSerializer, UsersLimitedSerializer


class DtpStudiesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpStudies
        fields = '__all__'


class DtpStudiesOutputSerializer(serializers.ModelSerializer):
    md_check_status = CheckStatusTypesOutputSerializer(many=False, read_only=True)
    md_check_by = UsersLimitedSerializer(many=False, read_only=True)
    study = StudyMainDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = DtpStudies
        fields = '__all__'
