import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.study_relationship_types import StudyRelationshipTypes
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyRelationships(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_relationships', default=None, null=True, blank=True)
    relationship_type = models.ForeignKey(StudyRelationshipTypes, on_delete=models.CASCADE,
                                          db_column='relationship_type_id', default=None, null=True, blank=True,
                                          related_name='study_relationships_relationship_type_id',
                                          db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    target_study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='target_study_id',
                                        related_name='study_relationships_target_study_id', default=None, null=True,
                                        blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       related_name='study_relationships_last_edited_by', default=None, null=True,
                                       blank=True, db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'study_relationships'
        ordering = ['created_on']
