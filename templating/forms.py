from django.forms import ModelForm

from templating.models import Template


class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'description', 'git_url']
