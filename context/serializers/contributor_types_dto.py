from rest_framework import serializers

from context.models.contributor_types import ContributorTypes


class ContributorTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorTypes
        fields = '__all__'


class ContributorTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorTypes
        fields = '__all__'
