from rest_framework import serializers

from context.models.study_types import StudyTypes


class StudyTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTypes
        fields = '__all__'


class StudyTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTypes
        fields = '__all__'
