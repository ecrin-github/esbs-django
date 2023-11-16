import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dup.dups import DataUseProcesses
from users.models import Users


class DataUseAccesses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_index=True,
                               related_name='dua_dup_id', default=None, null=True, blank=True, db_column='dup_id')
    conforms_to_default = models.BooleanField(default=False, db_index=True)
    variations = models.TextField(blank=True, null=True)
    repo_is_proxy_provider = models.BooleanField(default=False, db_index=True)
    dua_file_path = models.TextField(blank=True, null=True)
    repo_signatory_1 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='repo_signatory_1', null=False,
                                         related_name='dua_repo_signatory_1', default=None,
                                         db_constraint=IS_USERS_DB_CONSTRAINT)
    repo_signatory_2 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='repo_signatory_2', null=False,
                                         related_name='dua_repo_signatory_2', default=None,
                                         db_constraint=IS_USERS_DB_CONSTRAINT)
    provider_signatory_1 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='provider_signatory_1', null=False,
                                             related_name='dua_provider_signatory_1', default=None,
                                             db_constraint=IS_USERS_DB_CONSTRAINT)
    provider_signatory_2 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='provider_signatory_2', null=False,
                                             related_name='dua_provider_signatory_2', default=None,
                                             db_constraint=IS_USERS_DB_CONSTRAINT)
    requester_signatory_1 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='requester_signatory_1', null=False,
                                              related_name='dua_requester_signatory_1', default=None,
                                              db_constraint=IS_USERS_DB_CONSTRAINT)
    requester_signatory_2 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='requester_signatory_2', null=False,
                                              related_name='dua_requester_signatory_2', default=None,
                                              db_constraint=IS_USERS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_use_accesses'
        ordering = ['created_on']
