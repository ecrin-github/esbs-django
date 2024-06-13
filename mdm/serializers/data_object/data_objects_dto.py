from rest_framework import serializers

from context.serializers.doi_status_types_dto import DoiStatusTypesOutputSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesOutputSerializer
from context.serializers.object_classes_dto import ObjectClassesOutputSerializer
from context.serializers.object_types_dto import ObjectTypesOutputSerializer
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.data_object.data_objects import DataObjects
from mdm.serializers.data_object.object_contributors_dto import ObjectContributorsOutputSerializer
from mdm.serializers.data_object.object_datasets_dto import ObjectDatasetsOutputSerializer
from mdm.serializers.data_object.object_dates_dto import ObjectDatesOutputSerializer
from mdm.serializers.data_object.object_descriptions_dto import ObjectDescriptionsOutputSerializer
from mdm.serializers.data_object.object_identifiers_dto import ObjectIdentifiersOutputSerializer
from mdm.serializers.data_object.object_instances_dto import ObjectInstancesOutputSerializer
from mdm.serializers.data_object.object_relationships_dto import ObjectRelationshipsOutputSerializer
from mdm.serializers.data_object.object_rights_dto import ObjectRightsOutputSerializer
from mdm.serializers.data_object.object_titles_dto import ObjectTitlesOutputSerializer
from mdm.serializers.data_object.object_topics_dto import ObjectTopicsOutputSerializer
from mdm.serializers.study.study_main_details_dto import StudyMainDetailsSerializer
from mdm.models.data_object.object_number_sequence import ObjectNumberSeq
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class DataObjectsInputSerializerCreate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = DataObjects
        fields = '__all__'

    def to_internal_value(self, data):
        # Before insert - get DO ID here to avoid concurrency
        data['sd_oid'] = f'DSRO-{ObjectNumberSeq.objects.raw("select 1 as id, last_value from object_number_seq")[0].last_value}'
        return super().to_internal_value(data)


class DataObjectsInputSerializerUpdate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = DataObjects
        # Not updating sd_oid
        exclude = ['sd_oid']


class DataObjectsOutputSerializer(serializers.ModelSerializer):
    doi_status = DoiStatusTypesOutputSerializer(many=False, read_only=True)
    object_class = ObjectClassesOutputSerializer(many=False, read_only=True)
    object_type = ObjectTypesOutputSerializer(many=False, read_only=True)
    managing_org = OrganisationsOutputSerializer(many=False, read_only=True)
    lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    access_type = ObjectAccessTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)

    object_contributors = ObjectContributorsOutputSerializer(many=True, read_only=True)
    object_datasets = ObjectDatasetsOutputSerializer(many=True, read_only=True)
    object_dates = ObjectDatesOutputSerializer(many=True, read_only=True)
    object_descriptions = ObjectDescriptionsOutputSerializer(many=True, read_only=True)
    object_identifiers = ObjectIdentifiersOutputSerializer(many=True, read_only=True)
    object_instances = ObjectInstancesOutputSerializer(many=True, read_only=True)
    object_relationships = ObjectRelationshipsOutputSerializer(many=True, read_only=True)
    object_rights = ObjectRightsOutputSerializer(many=True, read_only=True)
    object_titles = ObjectTitlesOutputSerializer(many=True, read_only=True)
    object_topics = ObjectTopicsOutputSerializer(many=True, read_only=True)

    linked_study = StudyMainDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = DataObjects
        fields = ['id', 'sd_oid', 'display_title', 'version', 'doi', 'publication_year', 'access_details',
                  'access_details_url', 'url_last_checked', 'add_study_contributors',
                  'add_study_topics', 'created_on', 'organisation',
                  'doi_status', 'object_class', 'object_type', 'managing_org', 'lang_code', 'access_type',
                  'last_edited_by', 'object_contributors', 'object_datasets', 'object_dates', 'object_descriptions',
                  'object_identifiers', 'object_instances', 'object_relationships', 'object_rights', 'object_titles',
                  'object_topics', 'linked_study']
