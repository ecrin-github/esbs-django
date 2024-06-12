from rest_framework import serializers

from rms.models.dup.dup_studies import DupStudies
from mdm.serializers.study.study_main_details_dto import StudyMainDetailsSerializer


class DupStudiesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStudies
        fields = '__all__'


class DupStudiesOutputSerializer(serializers.ModelSerializer):
    study = StudyMainDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = DupStudies
        fields = '__all__'
