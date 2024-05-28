from django.db import models


class ObjectNumberSeq(models.Model):
    """
    This class maps to object_number_seq which is a PostgreSQL sequence.
    This sequence starts at 1 and cycles back to 1 after hitting 9223372036854775807.
    """
    last_value = models.IntegerField()
    increment_by = models.IntegerField()
    max_value = models.IntegerField()
    min_value = models.IntegerField()
    cache_value = models.IntegerField()
    log_cnt = models.IntegerField()
    is_cycled = models.BooleanField()
    is_called = models.BooleanField()

    class Meta:
        db_table = u'object_number_seq'