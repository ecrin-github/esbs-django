from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

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
from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from context.serializers.check_status_types_dto import CheckStatusTypesOutputSerializer
from context.serializers.composite_hash_types_dto import CompositeHashTypesOutputSerializer
from context.serializers.contributor_types_dto import ContributorTypesOutputSerializer
from context.serializers.dataset_consent_types_dto import DatasetConsentTypesOutputSerializer
from context.serializers.dataset_deidentification_levels_dto import DatasetDeidentificationLevelsOutputSerializer
from context.serializers.dataset_recordkey_types_dto import DatasetRecordkeyTypesOutputSerializer
from context.serializers.date_types_dto import DateTypesOutputSerializer
from context.serializers.description_types_dto import DescriptionTypesOutputSerializer
from context.serializers.doi_status_types_dto import DoiStatusTypesOutputSerializer
from context.serializers.dtp_status_types_dto import DtpStatusTypesOutputSerializer
from context.serializers.dup_status_types_dto import DupStatusTypesOutputSerializer
from context.serializers.gender_eligibility_types_dto import GenderEligibilityTypesOutputSerializer
from context.serializers.geog_entity_types_dto import GeogEntityTypesOutputSerializer
from context.serializers.identifier_types_dto import IdentifierTypesOutputSerializer
from context.serializers.language_usage_types_dto import LanguageUsageTypesOutputSerializer
from context.serializers.legal_status_types_dto import LegalStatusTypesOutputSerializer
from context.serializers.link_types_dto import LinkTypesOutputSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesOutputSerializer
from context.serializers.object_classes_dto import ObjectClassesOutputSerializer
from context.serializers.object_filter_types_dto import ObjectFilterTypesOutputSerializer
from context.serializers.object_instance_types_dto import ObjectInstanceTypesOutputSerializer
from context.serializers.object_relationship_types_dto import ObjectRelationshipTypesOutputSerializer
from context.serializers.object_types_dto import ObjectTypesOutputSerializer
from context.serializers.org_attribute_datatypes_dto import OrgAttributeDatatypesOutputSerializer
from context.serializers.org_attribute_types_dto import OrgAttributeTypesOutputSerializer
from context.serializers.org_classes_dto import OrgClassesOutputSerializer
from context.serializers.org_link_types_dto import OrgLinkTypesOutputSerializer
from context.serializers.org_names_qualifier_types_dto import OrgNameQualifierTypesOutputSerializer
from context.serializers.org_relationship_types_dto import OrgRelationshipTypesOutputSerializer
from context.serializers.org_types_dto import OrgTypesOutputSerializer
from context.serializers.prereq_types_dto import PrereqTypesOutputSerializer
from context.serializers.repo_access_types_dto import RepoAccessTypesOutputSerializer
from context.serializers.resource_types_dto import ResourceTypesOutputSerializer
from context.serializers.rms_user_types_dto import RmsUserTypesOutputSerializer
from context.serializers.role_classes_dto import RoleClassesOutputSerializer
from context.serializers.role_types_dto import RoleTypesOutputSerializer
from context.serializers.size_units_dto import SizeUnitsOutputSerializer
from context.serializers.study_feature_categories_dto import StudyFeatureCategoriesOutputSerializer
from context.serializers.study_feature_types_dto import StudyFeatureTypesOutputSerializer
from context.serializers.study_relationship_types_dto import StudyRelationshipTypesOutputSerializer
from context.serializers.study_statuses_dto import StudyStatusesOutputSerializer
from context.serializers.study_types_dto import StudyTypesOutputSerializer
from context.serializers.time_units_dto import TimeUnitsOutputSerializer
from context.serializers.title_types_dto import TitleTypesOutputSerializer
from context.serializers.topic_types_dto import TopicTypesOutputSerializer
from context.serializers.topic_vocabularies_dto import TopicVocabulariesOutputSerializer
from context.serializers.trial_registries_dto import TrialRegistriesOutputSerializer
from context.serializers.user_types_dto import UserTypesOutputSerializer


# Create your views here.
class AccessPrereqTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = AccessPrereqTypes.objects.all()
    serializer_class = AccessPrereqTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CheckStatusTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = CheckStatusTypes.objects.all()
    serializer_class = CheckStatusTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompositeHashTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = CompositeHashTypes.objects.all()
    serializer_class = CompositeHashTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContributorTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ContributorTypes.objects.all()
    serializer_class = ContributorTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetConsentTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DatasetConsentTypes.objects.all()
    serializer_class = DatasetConsentTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetDeidentificationLevelsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DatasetDeidentificationLevels.objects.all()
    serializer_class = DatasetDeidentificationLevelsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetRecordkeyTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DatasetRecordkeyTypes.objects.all()
    serializer_class = DatasetRecordkeyTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DateTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DateTypes.objects.all()
    serializer_class = DateTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DescriptionTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DescriptionTypes.objects.all()
    serializer_class = DescriptionTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DoiStatusTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DoiStatusTypes.objects.all()
    serializer_class = DoiStatusTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DtpStatusTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpStatusTypes.objects.all()
    serializer_class = DtpStatusTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DupStatusTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupStatusTypes.objects.all()
    serializer_class = DupStatusTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenderEligibilityTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = GenderEligibilityTypes.objects.all()
    serializer_class = GenderEligibilityTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GeogEntityTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = GeogEntityTypes.objects.all()
    serializer_class = GeogEntityTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IdentifierTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = IdentifierTypes.objects.all()
    serializer_class = IdentifierTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageUsageTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = LanguageUsageTypes.objects.all()
    serializer_class = LanguageUsageTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LegalStatusTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = LegalStatusTypes.objects.all()
    serializer_class = LegalStatusTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = LinkTypes.objects.all()
    serializer_class = LinkTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectAccessTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectAccessTypes.objects.all()
    serializer_class = ObjectAccessTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectClassesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectClasses.objects.all()
    serializer_class = ObjectClassesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectFilterTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectFilterTypes.objects.all()
    serializer_class = ObjectFilterTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectInstanceTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectInstanceTypes.objects.all()
    serializer_class = ObjectInstanceTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectRelationshipTypes.objects.all()
    serializer_class = ObjectRelationshipTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ObjectTypes.objects.all()
    serializer_class = ObjectTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributeDatatypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgAttributeDatatypes.objects.all()
    serializer_class = OrgAttributeDatatypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributeTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgAttributeTypes.objects.all()
    serializer_class = OrgAttributeTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgClassesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgClasses.objects.all()
    serializer_class = OrgClassesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgLinkTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgLinkTypes.objects.all()
    serializer_class = OrgLinkTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgNameQualifierTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgNameQualifierTypes.objects.all()
    serializer_class = OrgNameQualifierTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgRelationshipTypes.objects.all()
    serializer_class = OrgRelationshipTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = OrgTypes.objects.all()
    serializer_class = OrgTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PrereqTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = PrereqTypes.objects.all()
    serializer_class = PrereqTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RepoAccessTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = RepoAccessTypes.objects.all()
    serializer_class = RepoAccessTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResourceTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = ResourceTypes.objects.all()
    serializer_class = ResourceTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RmsUserTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = RmsUserTypes.objects.all()
    serializer_class = RmsUserTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleClassesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = RoleClasses.objects.all()
    serializer_class = RoleClassesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = RoleTypes.objects.all()
    serializer_class = RoleTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SizeUnitsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = SizeUnits.objects.all()
    serializer_class = SizeUnitsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyFeatureCategoriesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyFeatureCategories.objects.all()
    serializer_class = StudyFeatureCategoriesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyFeatureTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyFeatureTypes.objects.all()
    serializer_class = StudyFeatureTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyRelationshipTypes.objects.all()
    serializer_class = StudyRelationshipTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyStatusesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyStatuses.objects.all()
    serializer_class = StudyStatusesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = StudyTypes.objects.all()
    serializer_class = StudyTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimeUnitsList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = TimeUnits.objects.all()
    serializer_class = TimeUnitsOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TitleTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = TitleTypes.objects.all()
    serializer_class = TitleTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = TopicTypes.objects.all()
    serializer_class = TopicTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicVocabulariesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = TopicVocabularies.objects.all()
    serializer_class = TopicVocabulariesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrialRegistriesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = TrialRegistries.objects.all()
    serializer_class = TrialRegistriesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserTypesList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = UserTypes.objects.all()
    serializer_class = UserTypesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
