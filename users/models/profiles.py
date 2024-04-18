import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from context.models.rms_user_types import RmsUserTypes
from context.models.role_classes import RoleClasses
from context.models.role_types import RoleTypes
from general.models.organisations import Organisations
from users.models.users import Users


class UserProfiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='user_profile',
                                db_column='user_id', default=None, null=True, blank=True)
    ls_aai_id = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(RoleTypes, on_delete=models.CASCADE, db_column='role_id',
                             related_name='users_role_id', default=None, null=True, blank=True,
                             db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    role_class = models.ForeignKey(RoleClasses, on_delete=models.CASCADE, db_column='role_class_id',
                                   related_name='users_role_class', default='', null=True, blank=True,
                                   db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    user_type = models.ForeignKey(RmsUserTypes, on_delete=models.CASCADE, db_column='user_type_id',
                                  related_name='users_user_type', default=None, null=True, blank=True,
                                  db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='organisation_id',
                                     related_name='users_organisation_id', default=None, null=True, blank=True,
                                     db_constraint=IS_GENERAL_DB_CONSTRAINT)
    prof_title = models.CharField(max_length=25, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    inverted_full_name = models.CharField(max_length=255, null=True, blank=True)
    ocrid = models.CharField(max_length=75, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'user_profiles'
