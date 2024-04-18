import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from context.models.org_attribute_types import OrgAttributeTypes
from general.models.organisations import Organisations


class OrgAttributes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name="org_attributes_org_id", default=None, null=True, blank=True,
                                     db_column='organisation_id')
    attribute_type = models.ForeignKey(OrgAttributeTypes, on_delete=models.CASCADE, db_index=True,
                                       related_name="org_attributes_attribute_type_id", default=None, null=True,
                                       blank=True, db_column='attribute_type_id',
                                       db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    attribute_string_value = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    attribute_integer_value = models.IntegerField(blank=True, null=True, db_index=True)
    attribute_boolean_value = models.BooleanField(blank=True, null=True, db_index=True)
    attribute_date_value = models.DateField(blank=True, null=True, db_index=True)
    attribute_float_value = models.FloatField(blank=True, null=True, db_index=True)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'org_attributes'
        ordering = ["created_on"]
