from rest_framework import serializers

from context.models.trial_registries import TrialRegistries


class TrialRegistriesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialRegistries
        fields = '__all__'


class TrialRegistriesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialRegistries
        fields = '__all__'
