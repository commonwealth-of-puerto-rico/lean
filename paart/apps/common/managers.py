from django.db import models
from django.db.models.query import QuerySet


class OmitDisabledQuerySet(QuerySet):
    def active(self):
        return self.filter(enabled=True)


class OmitDisabledManager(models.Manager):
    def get_query_set(self):
        return OmitDisabledQuerySet(self.model, using=self._db)

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)
