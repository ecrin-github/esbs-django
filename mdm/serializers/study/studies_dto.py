from rest_framework import serializers

from context.serializers.gender_eligibility_types_dto import GenderEligibilityTypesOutputSerializer
from context.serializers.study_statuses_dto import StudyStatusesOutputSerializer
from context.serializers.study_types_dto import StudyTypesOutputSerializer
from context.serializers.time_units_dto import TimeUnitsOutputSerializer
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.study.studies import Studies
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer, DataObjectsLimitedOutputSerializer
from mdm.serializers.study.study_contributors_dto import StudyContributorsOutputSerializer, StudyContributorsLimitedOutputSerializer
from mdm.serializers.study.study_features_dto import StudyFeaturesOutputSerializer
from mdm.serializers.study.study_identifiers_dto import StudyIdentifiersOutputSerializer
from mdm.serializers.study.study_relationships_dto import StudyRelationshipsOutputSerializer
from mdm.serializers.study.study_titles_dto import StudyTitlesOutputSerializer
from mdm.serializers.study.study_topics_dto import StudyTopicsOutputSerializer
from mdm.models.study.study_number_sequence import StudyNumberSeq
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudiesInputSerializerCreate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = Studies
        fields = '__all__'

    def to_internal_value(self, data):
        # Before insert - get study ID here to avoid concurrency
        data['sd_sid'] = f'DSRS-{StudyNumberSeq.objects.raw("select 1 as id, last_value from study_number_seq")[0].last_value}'
        return super().to_internal_value(data)


class StudiesInputSerializerUpdate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = Studies
        # Not updating sd_sid
        exclude = ['sd_sid']


class StudiesOutputSerializer(serializers.ModelSerializer):
    title_lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    study_type = StudyTypesOutputSerializer(many=False, read_only=True)
    study_status = StudyStatusesOutputSerializer(many=False, read_only=True)
    study_gender_elig = GenderEligibilityTypesOutputSerializer(many=False, read_only=True)
    min_age_unit = TimeUnitsOutputSerializer(many=False, read_only=True)
    max_age_unit = TimeUnitsOutputSerializer(many=False, read_only=True)
    # last_edited_by = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)

    study_contributors = StudyContributorsOutputSerializer(many=True, read_only=True)
    study_features = StudyFeaturesOutputSerializer(many=True, read_only=True)
    study_identifiers = StudyIdentifiersOutputSerializer(many=True, read_only=True)
    study_relationships = StudyRelationshipsOutputSerializer(many=True, read_only=True)
    study_titles = StudyTitlesOutputSerializer(many=True, read_only=True)
    study_topics = StudyTopicsOutputSerializer(many=True, read_only=True)
    linked_objects = DataObjectsOutputSerializer(many=True, read_only=True)


    class Meta:
        model = Studies
        fields = ['id', 'sd_sid', 'display_title', 'title_lang_code', 'brief_description',
                  'data_sharing_statement', 'study_start_year', 'study_start_month', 'study_type',
                  'study_status', 'study_enrollment', 'study_gender_elig', 'min_age', 'min_age_unit',
                  'max_age', 'max_age_unit', 'created_on', 
                  'organisation', 'study_contributors', 'study_features',
                  'study_identifiers', 'study_relationships', 'study_titles', 'study_topics', 'linked_objects']


class StudiesLimitedOutputSerializer(serializers.ModelSerializer):
    title_lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    study_type = StudyTypesOutputSerializer(many=False, read_only=True)
    study_status = StudyStatusesOutputSerializer(many=False, read_only=True)
    study_gender_elig = GenderEligibilityTypesOutputSerializer(many=False, read_only=True)
    min_age_unit = TimeUnitsOutputSerializer(many=False, read_only=True)
    max_age_unit = TimeUnitsOutputSerializer(many=False, read_only=True)
    # last_edited_by = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)

    study_contributors = StudyContributorsLimitedOutputSerializer(many=True, read_only=True)
    study_features = StudyFeaturesOutputSerializer(many=True, read_only=True)
    study_identifiers = StudyIdentifiersOutputSerializer(many=True, read_only=True)
    study_relationships = StudyRelationshipsOutputSerializer(many=True, read_only=True)
    study_titles = StudyTitlesOutputSerializer(many=True, read_only=True)
    study_topics = StudyTopicsOutputSerializer(many=True, read_only=True)
    linked_objects = DataObjectsLimitedOutputSerializer(many=True, read_only=True)


    class Meta:
        model = Studies
        fields = ['id', 'sd_sid', 'display_title', 'title_lang_code', 'brief_description',
                  'data_sharing_statement', 'study_start_year', 'study_start_month', 'study_type',
                  'study_status', 'study_enrollment', 'study_gender_elig', 'min_age', 'min_age_unit',
                  'max_age', 'max_age_unit', 'created_on', 'organisation', 'study_contributors', 'study_features',
                  'study_identifiers', 'study_relationships', 'study_titles', 'study_topics', 'linked_objects']