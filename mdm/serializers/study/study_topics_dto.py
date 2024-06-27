from rest_framework import serializers

from context.serializers.topic_types_dto import TopicTypesOutputSerializer
from context.serializers.topic_vocabularies_dto import TopicVocabulariesOutputSerializer
from mdm.models.study.study_topics import StudyTopics
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudyTopicsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = StudyTopics
        fields = '__all__'


class StudyTopicsOutputSerializer(serializers.ModelSerializer):
    topic_type = TopicTypesOutputSerializer(many=False, read_only=True)
    # last_edited_by = UsersSerializer(many=False, read_only=True)
    original_value = TopicVocabulariesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = StudyTopics
        # fields = '__all__'
        exclude = ['last_edited_by']
