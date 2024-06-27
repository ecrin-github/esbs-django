import string
import random

from django.core.exceptions import BadRequest
from rest_framework import serializers

from general.models import Organisations
from users.models import UserProfiles
from users.models.users import Users
from users.serializers.create_user_class import CreateUserDto
from users.serializers.profiles_dto import UserProfilesOutputSerializer, UserProfilesLimitedOutputSerializer


class UsersSerializer(serializers.ModelSerializer):
    user_profile = UserProfilesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = Users
        fields = '__all__'


class UsersLimitedSerializer(serializers.ModelSerializer):
    user_profile = UserProfilesLimitedOutputSerializer(many=False, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'user_profile', 'email', 'first_name', 'last_name']


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    sub = serializers.CharField(required=False, max_length=500, allow_blank=True, default='')
    name = serializers.CharField(required=False, max_length=150, allow_blank=True, default='')
    family_name = serializers.CharField(required=False, max_length=75, allow_blank=True, default='')
    first_name = serializers.CharField(required=False, max_length=75, allow_blank=True, default='')
    last_name = serializers.CharField(required=False, max_length=75, allow_blank=True, default='')
    prof_title = serializers.CharField(required=False, max_length=100, allow_blank=True, default='')
    designation = serializers.CharField(required=False, max_length=100, allow_blank=True, default='')
    organisation = serializers.CharField(required=False, max_length=150, allow_blank=True, default='')
    is_superuser = serializers.BooleanField(required=False, default=False)

    def create(self, validated_data):
        user_dto = CreateUserDto(**validated_data)

        user_check = Users.objects.filter(email=user_dto.email)

        if user_check.exists():
            if user_dto.sub:
                user_data = Users.objects.get(email=user_dto.email)
                user_data.is_active = True
                user_data.save()
                user_profile_data_check = UserProfiles.objects.filter(user=user_data)
                if user_profile_data_check.exists():
                    user_profile_data = UserProfiles.objects.get(user=user_data)
                    user_profile_data.ls_aai_id = user_dto.sub
                    user_profile_data.save()
                else:
                    user_profile_data = UserProfiles(user=user_data, ls_aai_id=user_dto.sub)
                    user_profile_data.save()
                return CreateUserDto(**validated_data)
            else:
                raise BadRequest()

        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

        if user_dto.first_name or user_dto.last_name:
            user = Users(username=user_dto.email, email=user_dto.email, first_name=user_dto.first_name,
                         last_name=user_dto.last_name, is_superuser=user_dto.is_superuser, is_active=(user_dto.sub != ''))
        else:
            user = Users(username=user_dto.email, email=user_dto.email, last_name=user_dto.family_name,
                     first_name=user_dto.name.split(' ')[0], is_superuser=user_dto.is_superuser, is_active=(user_dto.sub != ''))

        email_split = user_dto.email.split('@')
        email_domain = email_split[1]
        if 'ecrin' in email_domain or 'ecrin.org' in email_domain or 'tsd' in email_domain:
            user.is_superuser = True
            user.is_staff = True

        user.set_password(password)
        user.save()

        added = False
        if user_dto.organisation:
            organisation = Organisations.objects.get(id=user_dto.organisation)
            if organisation:
                user_profile = UserProfiles(user=user, ls_aai_id=user_dto.sub, organisation=Organisations.objects.get(id=user_dto.organisation),
                                    prof_title=user_dto.prof_title, designation=user_dto.designation)
                added = True
        if not added:
            user_profile = UserProfiles(user=user, ls_aai_id=user_dto.sub, prof_title=user_dto.prof_title, designation=user_dto.designation)
        
        user_profile.save()

        return CreateUserDto(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.sub = validated_data.get('sub', instance.sub)
        instance.name = validated_data.get('name', instance.name)
        instance.family_name = validated_data.get('family_name', instance.family_name)
        instance.save()
        return instance
