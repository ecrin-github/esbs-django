from rest_framework import serializers

from context.models.repo_access_types import RepoAccessTypes


class RepoAccessTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepoAccessTypes
        fields = '__all__'


class RepoAccessTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepoAccessTypes
        fields = '__all__'
