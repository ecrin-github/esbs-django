from rest_framework import serializers

from general.models.published_journals import PublishedJournals


class PublishedJournalsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishedJournals
        fields = '__all__'


class PublishedJournalsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishedJournals
        fields = '__all__'
