from rest_framework import serializers

from context.models.topic_types import TopicTypes


class TopicTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTypes
        fields = '__all__'


class TopicTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTypes
        fields = '__all__'
