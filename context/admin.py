from django.contrib import admin

from context.models.access_prereq_types import AccessPrereqTypes
from context.models.check_status_types import CheckStatusTypes
from context.models.composite_hash_types import CompositeHashTypes
from context.models.contributor_types import ContributorTypes
from context.models.dataset_consent_types import DatasetConsentTypes
from context.models.dataset_deidentification_levels import DatasetDeidentificationLevels
from context.models.dataset_recordkey_types import DatasetRecordkeyTypes
from context.models.date_types import DateTypes
from context.models.description_types import DescriptionTypes
from context.models.doi_status_types import DoiStatusTypes
from context.models.dtp_status_types import DtpStatusTypes
from context.models.dup_status_types import DupStatusTypes
from context.models.gender_eligibility_types import GenderEligibilityTypes
from context.models.geog_entity_types import GeogEntityTypes
from context.models.identifier_types import IdentifierTypes
from context.models.language_usage_types import LanguageUsageTypes
from context.models.legal_status_types import LegalStatusTypes
from context.models.link_types import LinkTypes
from context.models.object_access_types import ObjectAccessTypes
from context.models.object_classes import ObjectClasses
from context.models.object_filter_types import ObjectFilterTypes
from context.models.object_instance_types import ObjectInstanceTypes
from context.models.object_relationship_types import ObjectRelationshipTypes
from context.models.object_types import ObjectTypes
from context.models.org_attribute_datatypes import OrgAttributeDatatypes
from context.models.org_attribute_types import OrgAttributeTypes
from context.models.org_classes import OrgClasses
from context.models.org_link_types import OrgLinkTypes
from context.models.org_names_qualifier_types import OrgNameQualifierTypes
from context.models.org_relationship_types import OrgRelationshipTypes
from context.models.org_types import OrgTypes
from context.models.prereq_types import PrereqTypes
from context.models.repo_access_types import RepoAccessTypes
from context.models.resource_types import ResourceTypes
from context.models.rms_user_types import RmsUserTypes
from context.models.role_classes import RoleClasses
from context.models.role_types import RoleTypes
from context.models.size_units import SizeUnits
from context.models.study_feature_categories import StudyFeatureCategories
from context.models.study_feature_types import StudyFeatureTypes
from context.models.study_relationship_types import StudyRelationshipTypes
from context.models.study_statuses import StudyStatuses
from context.models.study_types import StudyTypes
from context.models.time_units import TimeUnits
from context.models.title_types import TitleTypes
from context.models.topic_types import TopicTypes
from context.models.topic_vocabularies import TopicVocabularies
from context.models.trial_registries import TrialRegistries
from context.models.user_types import UserTypes


# Register your models here.
admin.site.register(AccessPrereqTypes)
admin.site.register(CheckStatusTypes)
admin.site.register(CompositeHashTypes)
admin.site.register(ContributorTypes)
admin.site.register(DatasetConsentTypes)
admin.site.register(DatasetDeidentificationLevels)
admin.site.register(DatasetRecordkeyTypes)
admin.site.register(DateTypes)
admin.site.register(DescriptionTypes)
admin.site.register(DoiStatusTypes)
admin.site.register(DtpStatusTypes)
admin.site.register(DupStatusTypes)
admin.site.register(GenderEligibilityTypes)
admin.site.register(GeogEntityTypes)
admin.site.register(IdentifierTypes)
admin.site.register(LanguageUsageTypes)
admin.site.register(LegalStatusTypes)
admin.site.register(LinkTypes)
admin.site.register(ObjectAccessTypes)
admin.site.register(ObjectClasses)
admin.site.register(ObjectFilterTypes)
admin.site.register(ObjectInstanceTypes)
admin.site.register(ObjectRelationshipTypes)
admin.site.register(ObjectTypes)
admin.site.register(OrgAttributeDatatypes)
admin.site.register(OrgAttributeTypes)
admin.site.register(OrgClasses)
admin.site.register(OrgLinkTypes)
admin.site.register(OrgNameQualifierTypes)
admin.site.register(OrgRelationshipTypes)
admin.site.register(OrgTypes)
admin.site.register(PrereqTypes)
admin.site.register(RepoAccessTypes)
admin.site.register(ResourceTypes)
admin.site.register(RmsUserTypes)
admin.site.register(RoleClasses)
admin.site.register(RoleTypes)
admin.site.register(SizeUnits)
admin.site.register(StudyFeatureCategories)
admin.site.register(StudyFeatureTypes)
admin.site.register(StudyRelationshipTypes)
admin.site.register(StudyStatuses)
admin.site.register(StudyTypes)
admin.site.register(TimeUnits)
admin.site.register(TitleTypes)
admin.site.register(TopicTypes)
admin.site.register(TopicVocabularies)
admin.site.register(TrialRegistries)
admin.site.register(UserTypes)
