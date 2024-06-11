import time

import psycopg2

import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent.__str__())

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esbs.settings')
django.setup()

from configs.esbs_db_settings import *
from context.models import CompositeHashTypes, AccessPrereqTypes, CheckStatusTypes, \
    ContributorTypes, \
    DatasetConsentTypes, DatasetDeidentificationLevels, DatasetRecordkeyTypes, \
    DateTypes, DescriptionTypes, \
    DoiStatusTypes, GenderEligibilityTypes, GeogEntityTypes, IdentifierTypes, \
    LanguageUsageTypes, LinkTypes, \
    ObjectAccessTypes, ObjectClasses, ObjectFilterTypes, ObjectInstanceTypes, \
    ObjectRelationshipTypes, ObjectTypes, \
    OrgAttributeDatatypes, OrgAttributeTypes, OrgClasses, OrgLinkTypes, \
    OrgNameQualifierTypes, OrgRelationshipTypes, \
    OrgTypes, ResourceTypes, RmsUserTypes, RoleClasses, RoleTypes, SizeUnits, \
    StudyFeatureTypes, StudyFeatureCategories, \
    StudyRelationshipTypes, StudyStatuses, StudyTypes, TimeUnits, TitleTypes, \
    TopicTypes, TopicVocabularies, \
    DtpStatusTypes, DupStatusTypes, LegalStatusTypes, PrereqTypes, RepoAccessTypes, \
    TrialRegistries, UserTypes

from general.models import PublishedJournals, MeshLookup, Organisations, LanguageCodes, GeogEntities

context_db_connection = psycopg2.connect(
    user=DEV_PG_USER_ESBS_DB,
    password=DEV_PG_PASSWORD_ESBS_DB,
    host=DEV_PG_HOST_ESBS_DB,
    port=DEV_PG_PORT_ESBS_DB,
    database=DEV_PG_DATABASE_ESBS_DB
)

rms_db_connection = context_db_connection


def get_data_from_table(db: str, schema: str, table_name: str):
    try:
        if db == 'context':
            if context_db_connection.closed:
                context_db_connection.reset()
            if not context_db_connection.closed:
                cursor = context_db_connection.cursor()
                cursor.execute(f"select * from {schema}.{table_name}")
                return cursor.fetchall()
        else:
            if rms_db_connection.closed:
                context_db_connection.reset()
            if not rms_db_connection.closed:
                cursor = rms_db_connection.cursor()
                cursor.execute(f"select * from {schema}.{table_name}")
                return cursor.fetchall()

    except Exception as error:
        print(f"failed: {error}")


def import_access_prereq_types():
    records = get_data_from_table('rms', 'rms', 'access_prereq_types')
    for rec in records:
        AccessPrereqTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3]
        )
    print("Access prereq types import finished")


def import_check_status_types():
    records = get_data_from_table('rms', 'lup', 'check_status_types')
    for rec in records:
        CheckStatusTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3]
        )
    print("Check status types import finished")


def import_composite_hash_types():
    records = get_data_from_table('context', 'lup', 'composite_hash_types')
    for rec in records:
        CompositeHashTypes.objects.create(
            name=rec[1],
            applies_to=rec[2],
            description=rec[3],
            list_order=rec[3],
            source=rec[4]
        )
    print("Composite hash types import finished")


def import_contributor_types():
    records = get_data_from_table('context', 'lup', 'contribution_types')
    for rec in records:
        ContributorTypes.objects.create(
            name=rec[1],
            applies_to=rec[2],
            description=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Contributor types import finished")


def import_dataset_consent_types():
    records = get_data_from_table('context', 'lup', 'dataset_consent_types')
    for rec in records:
        DatasetConsentTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Dataset consent types import finished")


def import_dataset_deidentification_levels():
    records = get_data_from_table('context', 'lup', 'dataset_deidentification_levels')
    for rec in records:
        DatasetDeidentificationLevels.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Deident level types import finished")


def import_dataset_recordkey_types():
    records = get_data_from_table('context', 'lup', 'dataset_recordkey_types')
    for rec in records:
        DatasetRecordkeyTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Dataset recordkey types import finished")


def import_date_types():
    records = get_data_from_table('context', 'lup', 'date_types')
    for rec in records:
        DateTypes.objects.create(
            name=rec[1],
            description=rec[2],
            applies_to_papers_only=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Date types import finished")


def import_description_types():
    records = get_data_from_table('context', 'lup', 'description_types')
    for rec in records:
        DescriptionTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Description types import finished")


def import_doi_status_types():
    records = get_data_from_table('context', 'lup', 'doi_status_types')
    for rec in records:
        DoiStatusTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("DOI status types import finished")


def import_gender_elig_types():
    records = get_data_from_table('context', 'lup', 'gender_eligibility_types')
    for rec in records:
        GenderEligibilityTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Gender elig types import finished")


def import_geog_entity_types():
    records = get_data_from_table('context', 'lup', 'geog_entity_types')
    for rec in records:
        GeogEntityTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Geog entity types import finished")


def import_identifier_types():
    records = get_data_from_table('context', 'lup', 'identifier_types')
    for rec in records:
        IdentifierTypes.objects.create(
            name=rec[1],
            applies_to=rec[2],
            description=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Identifier types import finished")


def import_language_usage_types():
    records = get_data_from_table('context', 'lup', 'language_usage_types')
    for rec in records:
        LanguageUsageTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Language usage types import finished")


def import_link_types():
    records = get_data_from_table('context', 'lup', 'link_types')
    for rec in records:
        LinkTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Link types import finished")


def import_object_access_types():
    records = get_data_from_table('context', 'lup', 'object_access_types')
    for rec in records:
        ObjectAccessTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Object access types import finished")


def import_object_classes():
    records = get_data_from_table('context', 'lup', 'object_classes')
    for rec in records:
        ObjectClasses.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Object classes import finished")


def import_object_filter_types():
    records = get_data_from_table('context', 'lup', 'object_filter_types')
    for rec in records:
        ObjectFilterTypes.objects.create(
            filter_as=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Object filter types import finished")


def import_object_instance_types():
    records = get_data_from_table('context', 'lup', 'object_instance_types')
    for rec in records:
        ObjectInstanceTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Object instance types import finished")


def import_object_relationship_types():
    records = get_data_from_table('context', 'lup', 'object_relationship_types')
    for rec in records:
        ObjectRelationshipTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Object relationship types import finished")


def import_object_types():
    global object_class, object_filter
    records = get_data_from_table('context', 'lup', 'object_types')

    object_classes = get_data_from_table('context', 'lup', 'object_classes')
    object_filter_types = get_data_from_table('context', 'lup', 'object_filter_types')

    for rec in records:
        for cls in object_classes:
            if cls[0] == rec[2]:
                object_class = ObjectClasses.objects.get(name=cls[1])
                break

        for obj_t in object_filter_types:
            if obj_t[0] == rec[3]:
                object_filter = ObjectFilterTypes.objects.get(filter_as=obj_t[1])
                break
        ObjectTypes.objects.create(
            name=rec[1],
            object_class=object_class,
            filter_as=object_filter,
            description=rec[4],
            use_in_data_entry=rec[5],
            list_order=rec[6],
            source=rec[7]
        )
    print("Object types import finished")


def import_org_attribute_datatypes():
    records = get_data_from_table('context', 'lup', 'org_attribute_datatypes')
    for rec in records:
        OrgAttributeDatatypes.objects.create(
            name=rec[1],
            list_order=rec[2],
        )
    print("Org attribute datatypes import finished")


def import_org_attribute_types():
    global org_datatype
    records = get_data_from_table('context', 'lup', 'org_attribute_types')
    org_attr_datatypes = get_data_from_table('context', 'lup', 'org_attribute_datatypes')

    for rec in records:
        for org_dt in org_attr_datatypes:
            if org_dt[0] == rec[2]:
                org_datatype = OrgAttributeDatatypes.objects.get(name=org_dt[1])
                break

        OrgAttributeTypes.objects.create(
            name=rec[1],
            org_attribute_datatype=org_datatype,
            description=rec[3],
            can_repeat=rec[4],
            parent_id=None,
            is_public=rec[6]
        )
    print("Org attribute types import finished")


def import_org_classes():
    records = get_data_from_table('context', 'lup', 'org_classes')
    for rec in records:
        OrgClasses.objects.create(
            name=rec[1],
            list_order=rec[2],
        )
    print("Org classes import finished")


def import_org_link_types():
    records = get_data_from_table('context', 'lup', 'org_link_types')
    for rec in records:
        OrgLinkTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3]
        )
    print("Org link types import finished")


def import_org_name_qualifier_types():
    records = get_data_from_table('context', 'lup', 'org_name_qualifier_types')
    for rec in records:
        OrgNameQualifierTypes.objects.create(
            name=rec[1],
            list_order=rec[2]
        )
    print("Org name qualifier types import finished")


def import_org_relationship_types():
    records = get_data_from_table('context', 'lup', 'org_relationship_types')
    for rec in records:
        OrgRelationshipTypes.objects.create(
            name=rec[1],
            list_order=rec[2]
        )
    print("Org relationship types import finished")


def import_org_types():
    global org_cls
    records = get_data_from_table('context', 'lup', 'org_types')
    org_classes = get_data_from_table('context', 'lup', 'org_classes')

    for rec in records:
        for org_cl in org_classes:
            if org_cl[0] == rec[2]:
                org_cls = OrgClasses.objects.get(name=org_cl[1])
                break

        OrgTypes.objects.create(
            name=rec[1],
        )
    print("Org types import finished")


def import_resource_types():
    records = get_data_from_table('context', 'lup', 'resource_types')
    for rec in records:
        ResourceTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Resource types import finished")


def import_rms_user_types():
    records = get_data_from_table('context', 'lup', 'rms_user_types')
    for rec in records:
        RmsUserTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("RMS user types import finished")


def import_role_classes():
    records = get_data_from_table('context', 'lup', 'role_classes')
    for rec in records:
        RoleClasses.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Role classes import finished")


def import_role_types():
    global role_class
    records = get_data_from_table('context', 'lup', 'role_types')
    role_classes = get_data_from_table('context', 'lup', 'role_classes')
    for rec in records:
        for role_cls in role_classes:
            if role_cls[0] == rec[2]:
                role_class = RoleClasses.objects.get(name=role_cls[1])
                break

        RoleTypes.objects.create(
            name=rec[1],
            role_class=role_class,
            list_order=rec[3]
        )
    print("Role types import finished")


def import_size_units():
    records = get_data_from_table('context', 'lup', 'size_units')
    for rec in records:
        SizeUnits.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Size units import finished")


def import_study_feature_types():
    records = get_data_from_table('context', 'lup', 'study_feature_types')
    for rec in records:
        StudyFeatureTypes.objects.create(
            context=rec[1],
            name=rec[2],
            description=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Study feature types import finished")


def import_study_feature_categories():
    global study_feature
    records = get_data_from_table('context', 'lup', 'study_feature_categories')
    study_feature_types = get_data_from_table('context', 'lup', 'study_feature_types')

    for rec in records:
        for sf in study_feature_types:
            if sf[0] == rec[1]:
                study_feature = StudyFeatureTypes.objects.get(name=sf[2])
                break

        StudyFeatureCategories.objects.create(
            feature_type=study_feature,
            name=rec[2],
            description=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Study feature categories import finished")


def import_study_relationship_types():
    records = get_data_from_table('context', 'lup', 'study_relationship_types')
    for rec in records:
        StudyRelationshipTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Study relationship types import finished")


def import_study_statuses():
    records = get_data_from_table('context', 'lup', 'study_statuses')
    for rec in records:
        StudyStatuses.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Study statuses import finished")


def import_study_types():
    records = get_data_from_table('context', 'lup', 'study_types')
    for rec in records:
        StudyTypes.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Study types import finished")


def import_time_units():
    records = get_data_from_table('context', 'lup', 'time_units')
    for rec in records:
        TimeUnits.objects.create(
            name=rec[1],
            description=rec[2],
            use_in_data_entry=rec[3],
            list_order=rec[4],
            source=rec[5]
        )
    print("Time units import finished")


def import_title_types():
    records = get_data_from_table('context', 'lup', 'title_types')
    for rec in records:
        TitleTypes.objects.create(
            name=rec[1],
            applies_to=rec[2],
            description=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Title types import finished")


def import_topic_types():
    records = get_data_from_table('context', 'lup', 'topic_types')
    for rec in records:
        TopicTypes.objects.create(
            name=rec[1],
            description=rec[2],
            value_type=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Topic types import finished")


def import_topic_vocabularies():
    records = get_data_from_table('context', 'lup', 'topic_vocabularies')
    for rec in records:
        TopicVocabularies.objects.create(
            name=rec[1],
            description=rec[2],
            url=rec[3],
            use_in_data_entry=rec[4],
            list_order=rec[5],
            source=rec[6]
        )
    print("Topic vocabularies import finished")


def import_dtp_status_types():
    records = get_data_from_table('rms', 'lup', 'dtp_status_types')
    for rec in records:
        DtpStatusTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("DTP status types import finished")


def import_dup_status_types():
    records = get_data_from_table('rms', 'lup', 'dup_status_types')
    for rec in records:
        DupStatusTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("DUP status types import finished")


def import_legal_status_types():
    records = get_data_from_table('rms', 'lup', 'legal_status_types')
    for rec in records:
        LegalStatusTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Legal status types import finished")


def import_prereq_types():
    records = get_data_from_table('rms', 'lup', 'prereq_types')
    for rec in records:
        PrereqTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Prereq types import finished")


def import_repo_access_types():
    records = get_data_from_table('rms', 'lup', 'repo_access_types')
    for rec in records:
        RepoAccessTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
        )
    print("Repo access types import finished")


def import_trial_registries():
    records = get_data_from_table('rms', 'lup', 'trial_registries')
    for rec in records:
        TrialRegistries.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("Trial registries import finished")


def import_published_journals():
    records = get_data_from_table('context', 'ctx', 'published_journals')
    for rec in records:
        PublishedJournals.objects.create(
            title=rec[0],
            publisher=rec[2],
            pisnn=rec[4],
            eisnn=rec[5],
            additional_issns=rec[6],
            doi=rec[7]
        )
    print("Published journals import finished")


def import_user_types():
    records = get_data_from_table('rms', 'lup', 'user_types')
    for rec in records:
        UserTypes.objects.create(
            name=rec[1],
            description=rec[2],
            list_order=rec[3],
            source=rec[4]
        )
    print("User types import finished")


def import_mesh_lookup():
    records = get_data_from_table('context', 'ctx', 'mesh_lookup')
    for rec in records:
        MeshLookup.objects.create(
            entry=rec[0],
            code=rec[1],
            term=rec[2],
            source=rec[3]
        )
    print("Mesh lookup import finished")


def import_organisations():
    records = get_data_from_table('rms', 'lup', 'organisations')
    for rec in records:
        Organisations.objects.create(
            default_name=rec[1],
            ror_id=rec[2],
            display_suffix=rec[3],
            scope_id=rec[4],
            scope_notes=rec[5],
            is_current=rec[6],
            year_established=rec[7],
            year_ceased=rec[8],
            city=rec[9],
            country_code=rec[10],
            country_name=rec[11]
        )
    print("Organisations import finished")


def import_languages():
    records = get_data_from_table('context', 'lup', 'language_codes')
    for rec in records:
        LanguageCodes.objects.create(
            language_code=rec[0],
            marc_code=rec[1],
            lang_name_en=rec[2],
            lang_name_fr=rec[3],
            lang_name_de=rec[4],
            source=rec[5]
        )
    print("Languages import finished")


def import_geog_entities():
    global geog_type
    records = get_data_from_table('context', 'ctx', 'geog_entities')
    geog_entity_types = get_data_from_table('context', 'lup', 'geog_entity_types')

    for rec in records:
        for geog_entity_type in geog_entity_types:
            if geog_entity_type[0] == rec[1]:
                geog_type = GeogEntityTypes.objects.get(name=geog_entity_type[1])
        GeogEntities.objects.create(
            name=rec[2],
            code=rec[3],
            parent=rec[5],
            old_id=rec[6],
            geog_entity_type=geog_type
        )
    print("Geog entities import finished")


def show_data():
    records = get_data_from_table('context', 'ctx', 'mesh_lookup')
    for rec in records:
        print(rec)

'''
# show_data()
import_access_prereq_types()
time.sleep(1.5)
import_check_status_types()
time.sleep(1.5)
#
import_composite_hash_types()
time.sleep(1.5)
#
import_contributor_types()
time.sleep(1.5)
#
import_dataset_consent_types()
time.sleep(1.5)
#
import_dataset_deidentification_levels()
time.sleep(1.5)
#
import_dataset_recordkey_types()
time.sleep(1.5)
#
import_date_types()
time.sleep(1.5)
#
import_description_types()
time.sleep(1.5)
#
import_doi_status_types()
time.sleep(1.5)
#
import_gender_elig_types()
time.sleep(1.5)
#
import_geog_entity_types()
time.sleep(1.5)
#
import_identifier_types()
time.sleep(1.5)
#
import_language_usage_types()
time.sleep(1.5)
#
import_link_types()
time.sleep(1.5)
#
import_object_access_types()
time.sleep(1.5)
#
import_object_classes()
time.sleep(1.5)
#
import_object_filter_types()
time.sleep(1.5)
#
import_object_instance_types()
time.sleep(1.5)
#
import_object_relationship_types()
time.sleep(1.5)
#
import_object_types()
time.sleep(1.5)
#
import_org_attribute_datatypes()
time.sleep(1.5)
import_org_attribute_types()
time.sleep(1.5)
import_org_classes()
time.sleep(1.5)
import_org_link_types()
time.sleep(1.5)
import_org_name_qualifier_types()
time.sleep(1.5)
import_org_relationship_types()
time.sleep(1.5)
import_org_types()
time.sleep(1.5)
import_resource_types()
time.sleep(1.5)
import_rms_user_types()
time.sleep(1.5)
import_role_classes()
time.sleep(1.5)
import_role_types()
time.sleep(1.5)
import_size_units()
time.sleep(1.5)
import_study_feature_types()
time.sleep(1.5)
import_study_feature_categories()
time.sleep(1.5)
import_study_relationship_types()
time.sleep(1.5)
import_study_statuses()
time.sleep(1.5)
import_study_types()
time.sleep(1.5)
import_time_units()
time.sleep(1.5)
import_title_types()
time.sleep(1.5)
import_topic_types()
time.sleep(1.5)
import_topic_vocabularies()
time.sleep(1.5)
import_dtp_status_types()
time.sleep(1.5)
import_dup_status_types()
time.sleep(1.5)
import_legal_status_types()
time.sleep(1.5)
import_prereq_types()
time.sleep(1.5)
import_repo_access_types()
time.sleep(1.5)
import_trial_registries()
time.sleep(1.5)
import_published_journals()
time.sleep(1.5)
import_user_types()
time.sleep(1.5)
import_mesh_lookup()
time.sleep(1.5)
import_organisations()
time.sleep(1.5)
import_languages()
time.sleep(1.5)
import_geog_entities()
time.sleep(1.5)

'''
