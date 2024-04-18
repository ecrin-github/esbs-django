import uuid

from django.db import models


class PublishedJournals(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    publisher = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    pisnn = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    eisnn = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    additional_issns = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    doi = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    class Meta:
        db_table = 'published_journals'
