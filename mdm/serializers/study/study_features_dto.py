from rest_framework import serializers

from context.serializers.study_feature_categories_dto import StudyFeatureCategoriesOutputSerializer
from context.serializers.study_feature_types_dto import StudyFeatureTypesOutputSerializer
from mdm.models.study.study_features import StudyFeatures
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudyFeaturesInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = StudyFeatures
        fields = '__all__'


class StudyFeaturesOutputSerializer(serializers.ModelSerializer):
    feature_type = StudyFeatureTypesOutputSerializer(many=False, read_only=True)
    feature_value = StudyFeatureCategoriesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyFeatures
        fields = '__all__'
