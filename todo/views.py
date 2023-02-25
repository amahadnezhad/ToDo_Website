from django.shortcuts import render
from django.views import generic

from .models import Task


class AboutUsView(generic.TemplateView):
    template_name = 'about.html'


def tasksview(request):  # Home
    items = Task.objects.all
    return render(request, 'home.html', {'items': items})