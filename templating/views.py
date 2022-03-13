from django.shortcuts import render, get_object_or_404

from templating.forms import TemplateForm
from templating.models import Template


def listing(request):
    templates = Template.objects.filter(published=True)
    return render(request, 'templating/listing.html', {
        'templates': templates
    })


def view(request, slug):
    template = get_object_or_404(Template, slug=slug)
    return render(request, f"{template.get_template_path()}/index.html")


def add(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TemplateForm()
    return render(request, 'templating/add.html', {
        'form': form
    })
