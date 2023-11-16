import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dtp.dtps import DataTransferProcesses
from users.models import Users


class DataTransferAccesses(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id',
                               related_name='dta_dtp_id', default=None, null=True, blank=True)
    conforms_to_default = models.BooleanField(default=False)
    variations = models.TextField(blank=True, null=True)
    dta_file_path = models.TextField(blank=True, null=True)
    repo_signature_1 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='repo_signature_1', null=False,
                                         related_name='dta_repo_signature_1', default=None,
                                         db_constraint=IS_USERS_DB_CONSTRAINT)
    repo_signature_2 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='repo_signature_2', null=False,
                                         related_name='dta_repo_signature_2', default=None,
                                         db_constraint=IS_USERS_DB_CONSTRAINT)
    provider_signature_1 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='provider_signature_1', null=False,
                                             related_name='dta_provider_signature_1', default=None,
                                             db_constraint=IS_USERS_DB_CONSTRAINT)
    provider_signature_2 = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='provider_signature_2', null=False,
                                             related_name='dta_provider_signature_2', default=None,
                                             db_constraint=IS_USERS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_transfer_accesses'
        ordering = ['created_on']
