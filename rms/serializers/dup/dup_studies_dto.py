from rest_framework import serializers

from rms.models.dup.dup_studies import DupStudies


class DupStudiesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStudies
        fields = '__all__'


class DupStudiesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStudies
        fields = '__all__'
