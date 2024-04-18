import uuid

from django.db import models

from context.models.org_classes import OrgClasses


class OrgTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    org_class = models.ForeignKey(OrgClasses, on_delete=models.CASCADE, db_column="class_id", db_index=True,
                                  related_name="org_types_class_id", default=None, null=True, blank=True)

    class Meta:
        db_table = "org_types"
        ordering = ["name"]
