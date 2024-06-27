from rest_framework import serializers

from context.serializers.language_usage_types_dto import LanguageUsageTypesOutputSerializer
from context.serializers.title_types_dto import TitleTypesOutputSerializer
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from mdm.models.data_object.object_titles import ObjectTitles
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectTitlesInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectTitles
        fields = '__all__'


class ObjectTitlesOutputSerializer(serializers.ModelSerializer):
    title_type = TitleTypesOutputSerializer(many=False, read_only=True)
    lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    lang_usage = LanguageUsageTypesOutputSerializer(many=False, read_only=True)
    # last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTitles
        # fields = '__all__'
        exclude = ['last_edited_by']
