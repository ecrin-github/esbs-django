from django.urls import path

from general.views.views import *


geog_entities_list = GeogEntitiesList.as_view({
    'get': 'list',
})
geog_entities_detail = GeogEntitiesList.as_view({
    'get': 'retrieve',
})

mesh_lookup_list = MeshLookupList.as_view({
    'get': 'list',
})
mesh_lookup_detail = MeshLookupList.as_view({
    'get': 'retrieve',
})

org_attributes_list = OrgAttributesList.as_view({
    'get': 'list',
})
org_attributes_detail = OrgAttributesList.as_view({
    'get': 'retrieve',
})

org_links_list = OrgLinksList.as_view({
    'get': 'list',
})
org_links_detail = OrgLinksList.as_view({
    'get': 'retrieve',
})

org_locations_list = OrgLocationsList.as_view({
    'get': 'list',
})
org_locations_detail = OrgLocationsList.as_view({
    'get': 'retrieve',
})

org_names_list = OrgNamesList.as_view({
    'get': 'list',
})
org_names_detail = OrgNamesList.as_view({
    'get': 'retrieve',
})

org_relationship_list = OrgRelationshipsList.as_view({
    'get': 'list',
})
org_relationship_detail = OrgRelationshipsList.as_view({
    'get': 'retrieve',
})

org_type_membership_list = OrgTypeMembershipList.as_view({
    'get': 'list',
})
org_type_membership_detail = OrgTypeMembershipList.as_view({
    'get': 'retrieve',
})

published_journals_list = PublishedJournalsList.as_view({
    'get': 'list',
})
published_journals_detail = PublishedJournalsList.as_view({
    'get': 'retrieve',
})

organisations_list = OrganisationsList.as_view({
    'get': 'list',
})
organisations_detail = OrganisationsList.as_view({
    'get': 'retrieve',
})

language_codes_list = LanguageCodesList.as_view({
    'get': 'list',
})
language_codes_detail = LanguageCodesList.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('geog-entities', geog_entities_list),
    path('geog-entities/<uuid:pk>', geog_entities_detail),

    path('mesh-lookup', mesh_lookup_list),
    path('mesh-lookup/<uuid:pk>', mesh_lookup_detail),

    path('organisations/<uuid:orgId>/org-attributes', org_attributes_list),
    path('organisations/<uuid:orgId>/org-attributes/<uuid:pk>', org_attributes_detail),

    path('organisations/<uuid:orgId>/org-links', org_links_list),
    path('organisations/<uuid:orgId>/org-links/<uuid:pk>', org_links_detail),

    path('organisations/<uuid:orgId>/org-locations', org_locations_list),
    path('organisations/<uuid:orgId>/org-locations/<uuid:pk>', org_locations_detail),

    path('organisations/<uuid:orgId>/org-names', org_names_list),
    path('organisations/<uuid:orgId>/org-names/<uuid:pk>', org_names_detail),

    path('organisations/<uuid:orgId>/org-relationships', org_relationship_list),
    path('organisations/<uuid:orgId>/org-relationships/<uuid:pk>', org_relationship_detail),

    path('organisations/<uuid:orgId>/org-type-membership', org_type_membership_list),
    path('organisations/<uuid:orgId>/org-type-membership/<uuid:pk>', org_type_membership_detail),

    path('published-journals', published_journals_list),
    path('published-journals/<uuid:pk>', published_journals_detail),

    path('language-codes', language_codes_list),
    path('language-codes/<uuid:pk>', language_codes_detail),

    path('organisations', organisations_list),
    path('organisations/<uuid:pk>', organisations_detail),
]
