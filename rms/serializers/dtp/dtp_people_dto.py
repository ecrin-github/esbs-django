from rest_framework import serializers

from rms.models.dtp.dtp_people import DtpPeople
from users.serializers.users_dto import UsersSerializer, UsersLimitedSerializer


class DtpPeopleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpPeople
        fields = '__all__'


class DtpPeopleOutputSerializer(serializers.ModelSerializer):
    person = UsersLimitedSerializer(many=False, read_only=True)

    class Meta:
        model = DtpPeople
        fields = '__all__'
