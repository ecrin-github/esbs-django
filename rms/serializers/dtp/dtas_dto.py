from rest_framework import serializers

from rms.models.dtp.dtas import DataTransferAccesses
from rms.serializers.dtp.dtp_people_dto import DtpPeopleOutputSerializer


class DataTransferAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAccesses
        fields = '__all__'


class DataTransferAccessesOutputSerializer(serializers.ModelSerializer):
    repo_signature1 = DtpPeopleOutputSerializer(many=False, read_only=True)
    repo_signature2 = DtpPeopleOutputSerializer(many=False, read_only=True)
    provider_signature1 = DtpPeopleOutputSerializer(many=False, read_only=True)
    provider_signature2 = DtpPeopleOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferAccesses
        fields = '__all__'
