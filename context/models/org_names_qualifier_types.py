import uuid

from django.db import models


class OrgNameQualifierTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    list_order = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "org_name_qualifier_types"
        ordering = ["list_order"]
