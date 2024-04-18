from rest_framework import serializers

from context.models.composite_hash_types import CompositeHashTypes


class CompositeHashTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositeHashTypes
        fields = '__all__'


class CompositeHashTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositeHashTypes
        fields = '__all__'
