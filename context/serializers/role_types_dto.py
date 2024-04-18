from rest_framework import serializers

from context.models.role_types import RoleTypes
from context.serializers.role_classes_dto import RoleClassesOutputSerializer


class RoleTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleTypes
        fields = '__all__'


class RoleTypesOutputSerializer(serializers.ModelSerializer):
    role_class = RoleClassesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = RoleTypes
        fields = '__all__'
