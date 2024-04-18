from rest_framework import serializers

from context.models.user_types import UserTypes


class UserTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = '__all__'


class UserTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = '__all__'
