from django.urls import path

from mdm.views.data_object.views import *
from mdm.views.study.views import *
from mdm.views.views import *


data_objects_list = DataObjectsList.as_view({
    'get': 'list',
    'post': 'create'
})
data_objects_detail = DataObjectsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_contributors_list = ObjectContributorsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_contributors_detail = ObjectContributorsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_datasets_list = ObjectDatasetsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_datasets_detail = ObjectDatasetsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_dates_list = ObjectDatesList.as_view({
    'get': 'list',
    'post': 'create'
})
object_dates_detail = ObjectDatesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_descriptions_list = ObjectDescriptionsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_descriptions_detail = ObjectDescriptionsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_identifiers_list = ObjectIdentifiersList.as_view({
    'get': 'list',
    'post': 'create'
})
object_identifiers_detail = ObjectIdentifiersList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_instances_list = ObjectInstancesList.as_view({
    'get': 'list',
    'post': 'create'
})
object_instances_detail = ObjectInstancesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_relationships_list = ObjectRelationshipsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_relationships_detail = ObjectRelationshipsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_rights_list = ObjectRightsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_rights_detail = ObjectRightsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_titles_list = ObjectTitlesList.as_view({
    'get': 'list',
    'post': 'create'
})
object_titles_detail = ObjectTitlesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

object_topics_list = ObjectTopicsList.as_view({
    'get': 'list',
    'post': 'create'
})
object_topics_detail = ObjectTopicsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

studies_list = StudiesList.as_view({
    'get': 'list',
    'post': 'create'
})
studies_detail = StudiesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_contributors_list = StudyContributorsList.as_view({
    'get': 'list',
    'post': 'create'
})
study_contributors_detail = StudyContributorsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_features_list = StudyFeaturesList.as_view({
    'get': 'list',
    'post': 'create'
})
study_features_detail = StudyFeaturesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_identifiers_list = StudyIdentifiersList.as_view({
    'get': 'list',
    'post': 'create'
})
study_identifiers_detail = StudyIdentifiersList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_relationships_list = StudyRelationshipsList.as_view({
    'get': 'list',
    'post': 'create'
})
study_relationships_detail = StudyRelationshipsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_titles_list = StudyTitlesList.as_view({
    'get': 'list',
    'post': 'create'
})
study_titles_detail = StudyTitlesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

study_topics_list = StudyTopicsList.as_view({
    'get': 'list',
    'post': 'create'
})
study_topics_detail = StudyTopicsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('data-objects', data_objects_list),
    path('data-objects/<uuid:pk>', data_objects_detail),

    path('data-objects/<uuid:objectId>/object-contributors', object_contributors_list),
    path('data-objects/<uuid:objectId>/object-contributors/<uuid:pk>', object_contributors_detail),

    path('data-objects/<uuid:objectId>/object-datasets', object_datasets_list),
    path('data-objects/<uuid:objectId>/object-datasets/<uuid:pk>', object_datasets_detail),

    path('data-objects/<uuid:objectId>/object-dates', object_dates_list),
    path('data-objects/<uuid:objectId>/object-dates/<uuid:pk>', object_dates_detail),

    path('data-objects/<uuid:objectId>/object-descriptions', object_descriptions_list),
    path('data-objects/<uuid:objectId>/object-descriptions/<uuid:pk>', object_descriptions_detail),

    path('data-objects/<uuid:objectId>/object-identifiers', object_identifiers_list),
    path('data-objects/<uuid:objectId>/object-identifiers/<uuid:pk>', object_identifiers_detail),

    path('data-objects/<uuid:objectId>/object-instances', object_instances_list),
    path('data-objects/<uuid:objectId>/object-instances/<uuid:pk>', object_instances_detail),

    path('data-objects/<uuid:objectId>/object-relationships', object_relationships_list),
    path('data-objects/<uuid:objectId>/object-relationships/<uuid:pk>', object_relationships_detail),

    path('data-objects/<uuid:objectId>/object-rights', object_rights_list),
    path('data-objects/<uuid:objectId>/object-rights/<uuid:pk>', object_rights_detail),

    path('data-objects/<uuid:objectId>/object-titles', object_titles_list),
    path('data-objects/<uuid:objectId>/object-titles/<uuid:pk>', object_titles_detail),

    path('data-objects/<uuid:objectId>/object-topics', object_topics_list),
    path('data-objects/<uuid:objectId>/object-topics/<uuid:pk>', object_topics_detail),

    path('studies', studies_list),
    path('studies/<uuid:pk>', studies_detail),

    path('studies/<uuid:studyId>/study-contributors', study_contributors_list),
    path('studies/<uuid:studyId>/study-contributors/<uuid:pk>', study_contributors_detail),

    path('studies/<uuid:studyId>/study-features', study_features_list),
    path('studies/<uuid:studyId>/study-features/<uuid:pk>', study_features_detail),

    path('studies/<uuid:studyId>/study-identifiers', study_identifiers_list),
    path('studies/<uuid:studyId>/study-identifiers/<uuid:pk>', study_identifiers_detail),

    path('studies/<uuid:studyId>/study-relationships', study_relationships_list),
    path('studies/<uuid:studyId>/study-relationships/<uuid:pk>', study_relationships_detail),

    path('studies/<uuid:studyId>/study-titles', study_titles_list),
    path('studies/<uuid:studyId>/study-titles/<uuid:pk>', study_titles_detail),

    path('studies/<uuid:studyId>/study-topics', study_topics_list),
    path('studies/<uuid:studyId>/study-topics/<uuid:pk>', study_topics_detail),

    path('studies/mdr/data', MdrStudiesData.as_view()),
    path('studies/mdr', MdrStudies.as_view()),
    path('studies/new-mdr', NewMdrStudies.as_view()),
    path('data-objects/mdr', MdrDataObjects.as_view()),

    path('studies/by-org', StudiesByOrg.as_view()),
    path('data-objects/by-org', DataObjectsByOrg.as_view()),
    path('dtp/by-org', DtpByOrg.as_view()),
    path('dup/by-org', DupByOrg.as_view()),

    path('dtp/object-involvement', DtpObjectInvolvement.as_view()),
    path('dup/object-involvement', DupObjectInvolvement.as_view()),

    path('dtp/study-involvement', DtpStudyInvolvement.as_view()),
    path('dup/study-involvement', DupStudyInvolvement.as_view()),

    path('multi-studies/objects', MultiStudiesObjects.as_view()),

    path('dtp/<uuid:dtpId>/study-involvement', DtpStudiesObjectsInvolvements.as_view()),
    path('dup/<uuid:dupId>/study-involvement', DupStudiesObjectsInvolvements.as_view()),
    path('dtp/<uuid:dtpId>/dup/<uuid:dupId>/study-involvement', DtpDupStudiesObjectsInvolvements.as_view()),

    path('studies/by-title', StudiesByTitle.as_view()),
    path('data-objects/by-title', DataObjectsByTitle.as_view()),
    path('dtp/by-title', DtpByTitle.as_view()),
    path('dup/by-title', DupByTitle.as_view()),
]
