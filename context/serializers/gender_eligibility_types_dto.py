from rest_framework import serializers

from context.models.gender_eligibility_types import GenderEligibilityTypes


class GenderEligibilityTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderEligibilityTypes
        fields = '__all__'


class GenderEligibilityTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderEligibilityTypes
        fields = '__all__'
