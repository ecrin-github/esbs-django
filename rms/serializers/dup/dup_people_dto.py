from rest_framework import serializers

from rms.models.dup.dup_people import DupPeople
from users.serializers.users_dto import UsersSerializer


class DupPeopleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupPeople
        fields = '__all__'


class DupPeopleOutputSerializer(serializers.ModelSerializer):
    person = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DupPeople
        fields = '__all__'
