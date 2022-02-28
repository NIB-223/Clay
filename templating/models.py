from django.conf import settings
from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    git_url = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    published = models.BooleanField(default=False)
    lighthouse_score = models.IntegerField(default=0)
