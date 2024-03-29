from rest_framework import serializers

from rms.models.dtp.dtas import DataTransferAccesses
from users.serializers.users_dto import UsersSerializer


class DataTransferAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAccesses
        fields = '__all__'


class DataTransferAccessesOutputSerializer(serializers.ModelSerializer):
    repo_signature1 = UsersSerializer(many=False, read_only=True)
    repo_signature2 = UsersSerializer(many=False, read_only=True)
    provider_signature1 = UsersSerializer(many=False, read_only=True)
    provider_signature2 = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferAccesses
        fields = '__all__'
