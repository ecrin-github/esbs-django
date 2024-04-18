from rest_framework import serializers

from context.models.link_types import LinkTypes


class LinkTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTypes
        fields = '__all__'


class LinkTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTypes
        fields = '__all__'
