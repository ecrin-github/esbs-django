from rest_framework import serializers

from context.models.topic_vocabularies import TopicVocabularies


class TopicVocabulariesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicVocabularies
        fields = '__all__'


class TopicVocabulariesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicVocabularies
        fields = '__all__'
