from rest_framework import serializers

from context.serializers.date_types_dto import DateTypesOutputSerializer
from mdm.models.data_object.object_dates import ObjectDates
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectDatesInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectDates
        fields = '__all__'


class ObjectDatesOutputSerializer(serializers.ModelSerializer):
    date_type = DateTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDates
        fields = '__all__'
