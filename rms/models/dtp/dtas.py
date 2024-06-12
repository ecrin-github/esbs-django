import datetime
import uuid

from django.db import models

from configs.rms_db_settings import IS_RMS_DB_CONSTRAINT
from rms.models.dtp.dtps import DataTransferProcesses
from rms.models.dtp.dtp_people import DtpPeople


class DataTransferAccesses(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id',
                               related_name='dta_dtp_id', default=None, null=True, blank=True)
    conforms_to_default = models.BooleanField(default=False)
    variations = models.TextField(blank=True, null=True)
    dta_file_path = models.TextField(blank=True, null=True)
    repo_signature1 = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='repo_signature_1', null=True,
                                        related_name='dta_repo_signature_1', default=None,
                                        db_constraint=IS_RMS_DB_CONSTRAINT)
    repo_signature2 = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='repo_signature_2', null=True,
                                        related_name='dta_repo_signature_2', default=None,
                                        db_constraint=IS_RMS_DB_CONSTRAINT)
    provider_signature1 = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='provider_signature_1', null=True,
                                            related_name='dta_provider_signature_1', default=None,
                                            db_constraint=IS_RMS_DB_CONSTRAINT)
    provider_signature2 = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='provider_signature_2', null=True,
                                            related_name='dta_provider_signature_2', default=None,
                                            db_constraint=IS_RMS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_transfer_accesses'
        ordering = ['created_on']
