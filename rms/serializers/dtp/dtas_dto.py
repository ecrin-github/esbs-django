from rest_framework import serializers

from rms.models.dtp.dtas import DataTransferAgreements
from rms.serializers.dtp.dtp_people_dto import DtpPeopleOutputSerializer


class DataTransferAgreementsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAgreements
        fields = '__all__'


class DataTransferAgreementsOutputSerializer(serializers.ModelSerializer):
    repo_signature1 = DtpPeopleOutputSerializer(many=False, read_only=True)
    repo_signature2 = DtpPeopleOutputSerializer(many=False, read_only=True)
    provider_signature1 = DtpPeopleOutputSerializer(many=False, read_only=True)
    provider_signature2 = DtpPeopleOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferAgreements
        fields = '__all__'
