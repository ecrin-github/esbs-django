import uuid

from django.db import models

from context.models.org_attribute_datatypes import OrgAttributeDatatypes


class OrgAttributeTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    org_attribute_datatype = models.ForeignKey(OrgAttributeDatatypes, on_delete=models.CASCADE, db_index=True,
                                               related_name="org_attribute_types_org_attribute_datatype_id",
                                               db_column='org_attribute_datatype_id', default=None, null=True,
                                               blank=True)
    can_repeat = models.BooleanField(default=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, db_index=True,
                                  related_name='org_attribute_types_parent_id', db_column='parent_id',
                                  default=None)
    is_public = models.BooleanField(default=False)

    class Meta:
        db_table = "org_attribute_types"
        ordering = ["name"]
