from django.contrib import admin

from general.models import GeogEntities
from general.models.language_codes import LanguageCodes
from general.models.mesh_lookup import MeshLookup
from general.models.org_attributes import OrgAttributes
from general.models.org_links import OrgLinks
from general.models.org_locations import OrgLocations
from general.models.org_names import OrgNames
from general.models.org_relationships import OrgRelationships
from general.models.org_type_membership import OrgTypeMembership
from general.models.organisations import Organisations
from general.models.published_journals import PublishedJournals

# Register your models here.
admin.site.register(GeogEntities)
admin.site.register(MeshLookup)
admin.site.register(LanguageCodes)
admin.site.register(OrgAttributes)
admin.site.register(OrgLinks)
admin.site.register(OrgLocations)
admin.site.register(OrgNames)
admin.site.register(OrgRelationships)
admin.site.register(OrgTypeMembership)
admin.site.register(Organisations)
admin.site.register(PublishedJournals)
