import json
import os

from django import template
from django.conf import settings

register = template.Library()

with open(os.path.join(settings.BASE_DIR, 'static', 'dist', 'manifest.json'), 'r') as f:
    manifest = json.load(f)


@register.simple_tag
def webpack(file):
    return manifest.get(file, None)
