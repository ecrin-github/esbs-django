from rest_framework import serializers

from context.models.study_feature_categories import StudyFeatureCategories
from context.serializers.study_feature_types_dto import StudyFeatureTypesOutputSerializer


class StudyFeatureCategoriesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyFeatureCategories
        fields = '__all__'


class StudyFeatureCategoriesOutputSerializer(serializers.ModelSerializer):
    feature_type = StudyFeatureTypesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = StudyFeatureCategories
        fields = '__all__'
