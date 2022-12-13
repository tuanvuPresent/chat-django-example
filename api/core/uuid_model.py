from django.db import models

from api.core.snowflake import UuidGenSingletonGroup


class UuidModel(models.Model):

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = UuidGenSingletonGroup(self.__class__).gen()
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
