import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.object_relationship_types import ObjectRelationshipTypes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectRelationships(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, db_index=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_relationships', default=None, null=True, blank=True)
    relationship_type = models.ForeignKey(ObjectRelationshipTypes, on_delete=models.CASCADE, db_index=True,
                                          related_name='object_relationships_relationship_type_id', default=None,
                                          null=True, blank=True, db_column='relationship_type_id',
                                          db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    target_object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_index=True,
                                         related_name='object_relationships_target_object_id', default=None, null=True,
                                         blank=True, db_column='target_object_id')
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_relationships_last_edited_by', default=None, null=True,
                                       blank=True, db_column='last_edited_by', db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'object_relationships'
        ordering = ['created_on']
