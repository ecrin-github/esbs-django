import uuid
import datetime

from django.db import models


class LanguageCodes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    language_code = models.CharField(max_length=3, unique=True, db_index=True)
    marc_code = models.CharField(max_length=10, unique=True, db_index=True)
    lang_name_en = models.CharField(max_length=50, db_index=True)
    lang_name_fr = models.CharField(max_length=50, db_index=True)
    lang_name_de = models.CharField(max_length=50, db_index=True)
    source = models.CharField(max_length=50, db_index=True)
    date_added = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "language_codes"
        ordering = ["language_code", "lang_name_en"]
