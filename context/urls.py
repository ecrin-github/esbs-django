from django.urls import path

from context.views.views import *


access_prereq_types_list = AccessPrereqTypesList.as_view({
    'get': 'list',
})
access_prereq_types_detail = AccessPrereqTypesList.as_view({
    'get': 'retrieve',
})

check_status_types_list = CheckStatusTypesList.as_view({
    'get': 'list',
})
check_status_types_detail = CheckStatusTypesList.as_view({
    'get': 'retrieve',
})

composite_hash_types_list = CompositeHashTypesList.as_view({
    'get': 'list',
})
composite_hash_types_detail = CompositeHashTypesList.as_view({
    'get': 'retrieve',
})

contributor_types_list = ContributorTypesList.as_view({
    'get': 'list',
})
contributor_types_detail = ContributorTypesList.as_view({
    'get': 'retrieve',
})

dataset_consent_types_list = DatasetConsentTypesList.as_view({
    'get': 'list',
})
dataset_consent_types_detail = DatasetConsentTypesList.as_view({
    'get': 'retrieve',
})

dataset_deidentification_levels_list = DatasetDeidentificationLevelsList.as_view({
    'get': 'list',
})
dataset_deidentification_levels_detail = DatasetDeidentificationLevelsList.as_view({
    'get': 'retrieve',
})

dataset_recordkey_types_list = DatasetRecordkeyTypesList.as_view({
    'get': 'list',
})
dataset_recordkey_types_detail = DatasetRecordkeyTypesList.as_view({
    'get': 'retrieve',
})

date_types_list = DateTypesList.as_view({
    'get': 'list',
})
date_types_detail = DateTypesList.as_view({
    'get': 'retrieve',
})

description_types_list = DescriptionTypesList.as_view({
    'get': 'list',
})
description_types_detail = DescriptionTypesList.as_view({
    'get': 'retrieve',
})

doi_status_types_list = DoiStatusTypesList.as_view({
    'get': 'list',
})
doi_status_types_detail = DoiStatusTypesList.as_view({
    'get': 'retrieve',
})

dtp_status_types_list = DtpStatusTypesList.as_view({
    'get': 'list',
})
dtp_status_types_detail = DtpStatusTypesList.as_view({
    'get': 'retrieve',
})

dup_status_types_list = DupStatusTypesList.as_view({
    'get': 'list',
})
dup_status_types_detail = DupStatusTypesList.as_view({
    'get': 'retrieve',
})

gender_eligibility_types_list = GenderEligibilityTypesList.as_view({
    'get': 'list',
})
gender_eligibility_types_detail = GenderEligibilityTypesList.as_view({
    'get': 'retrieve',
})

geog_entity_types_list = GeogEntityTypesList.as_view({
    'get': 'list',
})
geog_entity_types_detail = GeogEntityTypesList.as_view({
    'get': 'retrieve',
})

identifier_types_list = IdentifierTypesList.as_view({
    'get': 'list',
})
identifier_types_detail = IdentifierTypesList.as_view({
    'get': 'retrieve',
})

language_usage_types_list = LanguageUsageTypesList.as_view({
    'get': 'list',
})
language_usage_types_detail = LanguageUsageTypesList.as_view({
    'get': 'retrieve',
})

legal_status_types_list = LegalStatusTypesList.as_view({
    'get': 'list',
})
legal_status_types_detail = LegalStatusTypesList.as_view({
    'get': 'retrieve',
})

link_types_list = LinkTypesList.as_view({
    'get': 'list',
})
link_types_detail = LinkTypesList.as_view({
    'get': 'retrieve',
})

object_access_types_list = ObjectAccessTypesList.as_view({
    'get': 'list',
})
object_access_types_detail = ObjectAccessTypesList.as_view({
    'get': 'retrieve',
})

object_classes_list = ObjectClassesList.as_view({
    'get': 'list',
})
object_classes_detail = ObjectClassesList.as_view({
    'get': 'retrieve',
})

object_filter_types_list = ObjectFilterTypesList.as_view({
    'get': 'list',
})
object_filter_types_detail = ObjectFilterTypesList.as_view({
    'get': 'retrieve',
})

object_instance_types_list = ObjectInstanceTypesList.as_view({
    'get': 'list',
})
object_instance_types_detail = ObjectInstanceTypesList.as_view({
    'get': 'retrieve',
})

object_relationship_types_list = ObjectRelationshipTypesList.as_view({
    'get': 'list',
})
object_relationship_types_detail = ObjectRelationshipTypesList.as_view({
    'get': 'retrieve',
})

object_types_list = ObjectTypesList.as_view({
    'get': 'list',
})
object_types_detail = ObjectTypesList.as_view({
    'get': 'retrieve',
})

org_attribute_datatypes_list = OrgAttributeDatatypesList.as_view({
    'get': 'list',
})
org_attribute_datatypes_detail = OrgAttributeDatatypesList.as_view({
    'get': 'retrieve',
})

org_attribute_types_list = OrgAttributeTypesList.as_view({
    'get': 'list',
})
org_attribute_types_detail = OrgAttributeTypesList.as_view({
    'get': 'retrieve',
})

org_classes_list = OrgClassesList.as_view({
    'get': 'list',
})
org_classes_detail = OrgClassesList.as_view({
    'get': 'retrieve',
})

org_link_types_list = OrgLinkTypesList.as_view({
    'get': 'list',
})
org_link_types_detail = OrgLinkTypesList.as_view({
    'get': 'retrieve',
})

org_names_qualifier_types_list = OrgNameQualifierTypesList.as_view({
    'get': 'list',
})
org_names_qualifier_types_detail = OrgNameQualifierTypesList.as_view({
    'get': 'retrieve',
})

org_relationship_types_list = OrgRelationshipTypesList.as_view({
    'get': 'list',
})
org_relationship_types_detail = OrgRelationshipTypesList.as_view({
    'get': 'retrieve',
})

org_types_list = OrgTypesList.as_view({
    'get': 'list',
})
org_types_detail = OrgTypesList.as_view({
    'get': 'retrieve',
})

prereq_types_list = PrereqTypesList.as_view({
    'get': 'list',
})
prereq_types_detail = PrereqTypesList.as_view({
    'get': 'retrieve',
})

repo_access_types_list = RepoAccessTypesList.as_view({
    'get': 'list',
})
repo_access_types_detail = RepoAccessTypesList.as_view({
    'get': 'retrieve',
})

resource_types_list = ResourceTypesList.as_view({
    'get': 'list',
})
resource_types_detail = ResourceTypesList.as_view({
    'get': 'retrieve',
})

rms_user_types_list = RmsUserTypesList.as_view({
    'get': 'list',
})
rms_user_types_detail = RmsUserTypesList.as_view({
    'get': 'retrieve',
})

role_classes_list = RoleClassesList.as_view({
    'get': 'list',
})
role_classes_detail = RoleClassesList.as_view({
    'get': 'retrieve',
})

role_types_list = RoleTypesList.as_view({
    'get': 'list',
})
role_types_detail = RoleTypesList.as_view({
    'get': 'retrieve',
})

size_units_list = SizeUnitsList.as_view({
    'get': 'list',
})
size_units_detail = SizeUnitsList.as_view({
    'get': 'retrieve',
})

study_feature_categories_list = StudyFeatureCategoriesList.as_view({
    'get': 'list',
})
study_feature_categories_detail = StudyFeatureCategoriesList.as_view({
    'get': 'retrieve',
})

study_feature_types_list = StudyFeatureTypesList.as_view({
    'get': 'list',
})
study_feature_types_detail = StudyFeatureTypesList.as_view({
    'get': 'retrieve',
})

study_relationship_types_list = StudyRelationshipTypesList.as_view({
    'get': 'list',
})
study_relationship_types_detail = StudyRelationshipTypesList.as_view({
    'get': 'retrieve',
})

study_statuses_list = StudyStatusesList.as_view({
    'get': 'list',
})
study_statuses_detail = StudyStatusesList.as_view({
    'get': 'retrieve',
})

study_types_list = StudyTypesList.as_view({
    'get': 'list',
})
study_types_detail = StudyTypesList.as_view({
    'get': 'retrieve',
})

time_units_list = TimeUnitsList.as_view({
    'get': 'list',
})
time_units_detail = TimeUnitsList.as_view({
    'get': 'retrieve',
})

title_types_list = TitleTypesList.as_view({
    'get': 'list',
})
title_types_detail = TitleTypesList.as_view({
    'get': 'retrieve',
})

topic_types_list = TopicTypesList.as_view({
    'get': 'list',
})
topic_types_detail = TopicTypesList.as_view({
    'get': 'retrieve',
})

topic_vocabularies_list = TopicVocabulariesList.as_view({
    'get': 'list',
})
topic_vocabularies_detail = TopicVocabulariesList.as_view({
    'get': 'retrieve',
})

trial_registries_list = TrialRegistriesList.as_view({
    'get': 'list',
})
trial_registries_detail = TrialRegistriesList.as_view({
    'get': 'retrieve',
})

user_types_list = UserTypesList.as_view({
    'get': 'list',
})
user_types_detail = UserTypesList.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('access-prereq-types', access_prereq_types_list),
    path('access-prereq-types/<uuid:pk>', access_prereq_types_detail),

    path('check-status-types', check_status_types_list),
    path('check-status-types/<uuid:pk>', check_status_types_detail),

    path('composite-hash-types', composite_hash_types_list),
    path('composite-hash-types/<uuid:pk>', composite_hash_types_detail),

    path('contributor-types', contributor_types_list),
    path('contributor-types/<uuid:pk>', contributor_types_detail),

    path('dataset-consent-types', dataset_consent_types_list),
    path('dataset-consent-types/<uuid:pk>', dataset_consent_types_detail),

    path('dataset-deidentification-levels', dataset_deidentification_levels_list),
    path('dataset-deidentification-levels/<uuid:pk>', dataset_deidentification_levels_detail),

    path('dataset-recordkey-types', dataset_recordkey_types_list),
    path('dataset-recordkey-types/<uuid:pk>', dataset_recordkey_types_detail),

    path('date-types', date_types_list),
    path('date-types/<uuid:pk>', date_types_detail),

    path('description-types', description_types_list),
    path('description-types/<uuid:pk>', description_types_detail),

    path('doi-status-types', doi_status_types_list),
    path('doi-status-types/<uuid:pk>', doi_status_types_detail),

    path('dtp-status-types', dtp_status_types_list),
    path('dtp-status-types/<uuid:pk>', dtp_status_types_detail),

    path('dup-status-types', dup_status_types_list),
    path('dup-status-types/<uuid:pk>', dup_status_types_detail),

    path('gender-eligibility-types', gender_eligibility_types_list),
    path('gender-eligibility-types/<uuid:pk>', gender_eligibility_types_detail),

    path('geog-entity-types', geog_entity_types_list),
    path('geog-entity-types/<uuid:pk>', geog_entity_types_detail),

    path('identifier-types', identifier_types_list),
    path('identifier-types/<uuid:pk>', identifier_types_detail),

    path('language-usage-types', language_usage_types_list),
    path('language-usage-types/<uuid:pk>', language_usage_types_detail),

    path('legal-status-types', legal_status_types_list),
    path('legal-status-types/<uuid:pk>', legal_status_types_detail),

    path('link-types', link_types_list),
    path('link-types/<uuid:pk>', link_types_detail),

    path('object-access-types', object_access_types_list),
    path('object-access-types/<uuid:pk>', object_access_types_detail),

    path('object-classes', object_classes_list),
    path('object-classes/<uuid:pk>', object_classes_detail),

    path('object-filter-types', object_filter_types_list),
    path('object-filter-types/<uuid:pk>', object_filter_types_detail),

    path('object-instance-types', object_instance_types_list),
    path('object-instance-types/<uuid:pk>', object_instance_types_detail),

    path('object-relationship-types', object_relationship_types_list),
    path('object-relationship-types/<uuid:pk>', object_relationship_types_detail),

    path('object-types', object_types_list),
    path('object-types/<uuid:pk>', object_types_detail),

    path('org-attribute-datatypes', org_attribute_datatypes_list),
    path('org-attribute-datatypes/<uuid:pk>', org_attribute_datatypes_detail),

    path('org-attribute-types', org_attribute_types_list),
    path('org-attribute-types/<uuid:pk>', org_attribute_types_detail),

    path('org-classes', org_classes_list),
    path('org-classes/<uuid:pk>', org_classes_detail),

    path('org-link-types', org_link_types_list),
    path('org-link-types/<uuid:pk>', org_link_types_detail),

    path('org-names-qualifier-types', org_names_qualifier_types_list),
    path('org-names-qualifier-types/<uuid:pk>', org_names_qualifier_types_detail),

    path('org-relationship-types', org_relationship_types_list),
    path('org-relationship-types/<uuid:pk>', org_relationship_types_detail),

    path('org-types', org_types_list),
    path('org-types/<uuid:pk>', org_types_detail),

    path('prereq-types', prereq_types_list),
    path('prereq-types/<uuid:pk>', prereq_types_detail),

    path('repo-access-types', repo_access_types_list),
    path('repo-access-types/<uuid:pk>', repo_access_types_detail),

    path('resource-types', resource_types_list),
    path('resource-types/<uuid:pk>', resource_types_detail),

    path('rms-user-types', rms_user_types_list),
    path('rms-user-types/<uuid:pk>', rms_user_types_detail),

    path('role-classes', role_classes_list),
    path('role-classes/<uuid:pk>', role_classes_detail),

    path('role-types', role_types_list),
    path('role-types/<uuid:pk>', role_types_detail),

    path('size-units', size_units_list),
    path('size-units/<uuid:pk>', size_units_detail),

    path('study-feature-categories', study_feature_categories_list),
    path('study-feature-categories/<uuid:pk>', study_feature_categories_detail),

    path('study-feature-types', study_feature_types_list),
    path('study-feature-types/<uuid:pk>', study_feature_types_detail),

    path('study-relationship-types', study_relationship_types_list),
    path('study-relationship-types/<uuid:pk>', study_relationship_types_detail),

    path('study-statuses', study_statuses_list),
    path('study-statuses/<uuid:pk>', study_statuses_detail),

    path('study-types', study_types_list),
    path('study-types/<uuid:pk>', study_types_detail),

    path('time-units', time_units_list),
    path('time-units/<uuid:pk>', time_units_detail),

    path('title-types', title_types_list),
    path('title-types/<uuid:pk>', title_types_detail),

    path('topic-types', topic_types_list),
    path('topic-types/<uuid:pk>', topic_types_detail),

    path('topic-vocabularies', topic_vocabularies_list),
    path('topic-vocabularies/<uuid:pk>', topic_vocabularies_detail),

    path('trial-registries', trial_registries_list),
    path('trial-registries/<uuid:pk>', trial_registries_detail),

    path('user-types', user_types_list),
    path('user-types/<uuid:pk>', user_types_detail),
]
