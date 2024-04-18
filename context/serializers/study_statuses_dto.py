from rest_framework import serializers

from context.models.study_statuses import StudyStatuses


class StudyStatusesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyStatuses
        fields = '__all__'


class StudyStatusesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyStatuses
        fields = '__all__'
