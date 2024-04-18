from rest_framework import serializers

from context.serializers.topic_types_dto import TopicTypesOutputSerializer
from context.serializers.topic_vocabularies_dto import TopicVocabulariesOutputSerializer
from mdm.models.data_object.object_topics import ObjectTopics
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectTopicsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectTopics
        fields = '__all__'


class ObjectTopicsOutputSerializer(serializers.ModelSerializer):
    topic_type = TopicTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)
    original_value = TopicVocabulariesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTopics
        fields = '__all__'
