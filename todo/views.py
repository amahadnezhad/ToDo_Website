from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from .models import Task
from .forms import ListForm


class AboutUsView(generic.TemplateView):
    template_name = 'about.html'


def tasksview(request):  # Home
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            items = Task.objects.all()
            messages.success(request, 'Item Has Been Added To List!')
            return render(request, 'home.html', {'items': items})
    else:
        items = Task.objects.all
        return render(request, 'home.html', {'items': items})
