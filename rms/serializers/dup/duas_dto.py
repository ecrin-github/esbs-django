from rest_framework import serializers

from rms.models.dup.duas import DataUseAgreements
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer


class DataUseAgreementsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAgreements
        fields = '__all__'


class DataUseAgreementsOutputSerializer(serializers.ModelSerializer):
    repo_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    repo_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)
    provider_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    provider_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)
    requester_signatory1 = DupPeopleOutputSerializer(many=False, read_only=True)
    requester_signatory2 = DupPeopleOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataUseAgreements
        fields = '__all__'
