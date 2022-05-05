from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


def home(request):
    return render(request=request, template_name='base.html')


@staff_member_required
def bootstrap(request):
    return render(request=request, template_name='bootstrap.html')
