import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.topic_types import TopicTypes
from context.models.topic_vocabularies import TopicVocabularies
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyTopics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_topics', default=None, null=True, blank=True)
    topic_type = models.ForeignKey(TopicTypes, on_delete=models.CASCADE, db_column='topic_type_id',
                                   related_name='study_topics_topic_type_id', default=None, null=True, blank=True,
                                   db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    mesh_coded = models.BooleanField(default=False)
    mesh_code = models.CharField(max_length=255, blank=True, null=True)
    mesh_value = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.ForeignKey(TopicVocabularies, on_delete=models.CASCADE, db_column='original_value', 
                                       related_name='study_topics_original_value', default=None, blank=True, null=True,
                                        db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       related_name='study_topics_last_edited_by', default=None, null=True, blank=True,
                                       db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'study_topics'
        ordering = ['created_on']
