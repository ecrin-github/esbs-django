from django.db import models


class MeshLookup(models.Model):
    entry = models.CharField(max_length=255, db_index=True)
    code = models.CharField(max_length=255, db_index=True)
    term = models.CharField(max_length=255, db_index=True)
    source = models.CharField(max_length=255, db_index=True)

    class Meta:
        db_table = 'mesh_lookup'
