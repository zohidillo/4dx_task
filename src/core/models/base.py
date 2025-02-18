from django.db import models
from django.contrib.auth.models import User


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_created_by', )
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='%(app_label)s_%(class)s_updated_by')

    objects = CustomManager()

    class Meta:
        abstract = True
