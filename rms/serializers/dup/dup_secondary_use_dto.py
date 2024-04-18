from rest_framework import serializers

from rms.models.dup.dup_secondary_use import DupSecondaryUse


class DupSecondaryUseInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupSecondaryUse
        fields = '__all__'


class DupSecondaryUseOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupSecondaryUse
        fields = '__all__'
