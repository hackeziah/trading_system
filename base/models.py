from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted= models.BooleanField(default=False)

    class Meta:
        abstract = True
        