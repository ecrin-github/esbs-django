import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.description_types import DescriptionTypes
from general.models.language_codes import LanguageCodes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectDescriptions(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, db_index=True, unique=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_descriptions', default=None, null=True, blank=True)
    description_type = models.ForeignKey(DescriptionTypes, on_delete=models.CASCADE, db_index=True,
                                         related_name='object_descriptions_description_type_id', default=None, null=True,
                                         blank=True, db_column='description_type_id',
                                         db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    description_text = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    lang_code = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_index=True,
                                  related_name='object_descriptions_lang_code_id', default=None, null=True, blank=True,
                                  db_column='lang_code_id', db_constraint=IS_GENERAL_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_descriptions_last_edited_by', default=None, null=True,
                                       blank=True, db_column='last_edited_by', db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'object_descriptions'
        ordering = ['created_on']
