from rest_framework import serializers

from rms.models.dtp.dtp_notes import DtpNotes
from users.serializers.users_dto import UsersSerializer, UsersLimitedSerializer


class DtpNotesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpNotes
        fields = '__all__'


class DtpNotesOutputSerializer(serializers.ModelSerializer):
    author = UsersLimitedSerializer(many=False, read_only=True)

    class Meta:
        model = DtpNotes
        fields = '__all__'
