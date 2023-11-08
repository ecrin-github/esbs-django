import string
import random

from rest_framework import serializers

from users.models import UserProfiles
from users.models.users import Users
from users.serializers.create_user_class import CreateUserDto
from users.serializers.profiles_dto import UserProfilesOutputSerializer


class UsersSerializer(serializers.ModelSerializer):
    user_profile = UserProfilesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = Users
        fields = '__all__'


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    sub = serializers.CharField(max_length=500)
    name = serializers.CharField(max_length=150)
    given_name = serializers.CharField(max_length=75)
    family_name = serializers.CharField(max_length=75)

    def create(self, validated_data):
        user_dto = CreateUserDto(**validated_data)

        user_check = Users.objects.filter(email=user_dto.email)
        if user_check.exists():
            return CreateUserDto(**validated_data)

        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        user = Users(username=user_dto.email, email=user_dto.email, last_name=user_dto.family_name,
                     first_name=user_dto.given_name, is_active=True)

        email_split = user_dto.email.split('@')
        email_domain = email_split[1]
        if 'ecrin' in email_domain or 'ecrin.org' in email_domain or 'tsd' in email_domain:
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        user.set_password(password)

        user.save()

        user_profile = UserProfiles(user=user, ls_aai_id=user_dto.sub)
        user_profile.save()

        return CreateUserDto(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.sub = validated_data.get('sub', instance.sub)
        instance.name = validated_data.get('name', instance.name)
        instance.given_name = validated_data.get('given_name', instance.given_name)
        instance.family_name = validated_data.get('family_name', instance.family_name)
        instance.save()
        return instance
