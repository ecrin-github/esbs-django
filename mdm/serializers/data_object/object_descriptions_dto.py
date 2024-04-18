from rest_framework import serializers

from context.serializers.description_types_dto import DescriptionTypesOutputSerializer
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from mdm.models.data_object.object_descriptions import ObjectDescriptions
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectDescriptionsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectDescriptions
        fields = '__all__'


class ObjectDescriptionsOutputSerializer(serializers.ModelSerializer):
    description_type = DescriptionTypesOutputSerializer(many=False, read_only=True)
    lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDescriptions
        fields = '__all__'
