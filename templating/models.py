import os

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from git import Repo


class Template(models.Model):
    TEMPLATES_DIR = os.path.join(settings.BASE_DIR, 'git_templates')

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

    def clone_repo(self):
        Repo.clone_from(self.git_url, self.get_template_path())

    def update_repo(self):
        repo = Repo(self.get_template_path())
        repo.remotes.origin.pull()

    def get_template_path(self):
        return os.path.join(self.TEMPLATES_DIR, self.slug)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            self.slug = slugify(self.name)
            self.clone_repo()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.name} - {self.git_url}"
