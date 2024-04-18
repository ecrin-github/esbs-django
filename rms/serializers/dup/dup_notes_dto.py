from rest_framework import serializers

from rms.models.dup.dup_notes import DupNotes
from users.serializers.users_dto import UsersSerializer


class DupNotesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupNotes
        fields = '__all__'


class DupNotesOutputSerializer(serializers.ModelSerializer):
    author = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DupNotes
        fields = '__all__'
