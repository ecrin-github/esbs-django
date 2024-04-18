import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from context.models.org_link_types import OrgLinkTypes
from general.models.organisations import Organisations


class OrgLinks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name="org_links_org_id", default=None, null=True, blank=True,
                                     db_column='organisation_id')
    org_link_type = models.ForeignKey(OrgLinkTypes, on_delete=models.CASCADE, db_index=True,
                                      related_name="org_links_org_link_type", default=None, null=True, blank=True,
                                      db_column='org_link_type_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    link = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow, db_index=True)

    class Meta:
        db_table = 'org_links'
        ordering = ['created_on']
