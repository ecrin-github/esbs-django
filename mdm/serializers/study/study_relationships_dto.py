from rest_framework import serializers

from context.serializers.study_relationship_types_dto import StudyRelationshipTypesOutputSerializer
from mdm.models.study.study_relationships import StudyRelationships
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudyRelationshipsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = StudyRelationships
        fields = '__all__'


class StudyRelationshipsOutputSerializer(serializers.ModelSerializer):
    relationship_type = StudyRelationshipTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyRelationships
        fields = '__all__'
