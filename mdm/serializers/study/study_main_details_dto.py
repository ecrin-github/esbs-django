from rest_framework import serializers

from mdm.models.study.studies import Studies


class StudyMainDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studies
        fields = ['id', 'sd_sid', 'display_title', 'brief_description', 'data_sharing_statement']