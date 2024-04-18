from rest_framework import serializers

from context.serializers.rms_user_types_dto import RmsUserTypesOutputSerializer
from context.serializers.role_classes_dto import RoleClassesOutputSerializer
from context.serializers.role_types_dto import RoleTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from users.models.profiles import UserProfiles


class UserProfilesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'


class UserProfilesOutputSerializer(serializers.ModelSerializer):
    role = RoleTypesOutputSerializer(many=False, read_only=True)
    role_class = RoleClassesOutputSerializer(many=False, read_only=True)
    user_type = RmsUserTypesOutputSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfiles
        fields = '__all__'
