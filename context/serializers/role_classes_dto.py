from rest_framework import serializers

from context.models.role_classes import RoleClasses


class RoleClassesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleClasses
        fields = '__all__'


class RoleClassesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleClasses
        fields = '__all__'
