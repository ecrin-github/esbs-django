from rest_framework import serializers

from context.models.study_relationship_types import StudyRelationshipTypes


class StudyRelationshipTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyRelationshipTypes
        fields = '__all__'


class StudyRelationshipTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyRelationshipTypes
        fields = '__all__'
