from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Template(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    git_url = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    published = models.BooleanField(default=False)
    lighthouse_score = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
