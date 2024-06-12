from rest_framework import serializers

from rms.models.dup.duas import DataUseAccesses
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer


class DataUseAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAccesses
        fields = '__all__'


class DataUseAccessesOutputSerializer(serializers.ModelSerializer):
    repo_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    repo_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)
    provider_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    provider_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)
    requester_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    requester_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataUseAccesses
        fields = '__all__'
