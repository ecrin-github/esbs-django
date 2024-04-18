from rest_framework import serializers

from rms.models.dup.duas import DataUseAccesses
from users.serializers.users_dto import UsersSerializer


class DataUseAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAccesses
        fields = '__all__'


class DataUseAccessesOutputSerializer(serializers.ModelSerializer):
    repo_signatory_1 = UsersSerializer(many=False, read_only=True)
    repo_signatory_2 = UsersSerializer(many=False, read_only=True)
    provider_signatory_1 = UsersSerializer(many=False, read_only=True)
    provider_signatory_2 = UsersSerializer(many=False, read_only=True)
    requester_signatory_1 = UsersSerializer(many=False, read_only=True)
    requester_signatory_2 = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DataUseAccesses
        fields = '__all__'
