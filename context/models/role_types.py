import uuid

from django.db import models

from context.models.role_classes import RoleClasses


class RoleTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    list_order = models.IntegerField(default=0, null=True)
    role_class = models.ForeignKey(RoleClasses, on_delete=models.CASCADE, db_index=True,
                                   related_name="role_types_role_class_id", db_column='role_class_id',
                                   default=None, null=True, blank=True)

    class Meta:
        db_table = "role_types"
        ordering = ["list_order"]
