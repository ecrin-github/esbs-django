from rest_framework import serializers

from mdm.models.data_object.object_rights import ObjectRights
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectRightsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectRights
        fields = '__all__'


class ObjectRightsOutputSerializer(serializers.ModelSerializer):
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectRights
        fields = '__all__'
