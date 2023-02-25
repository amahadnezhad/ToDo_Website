from django.shortcuts import render, redirect
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


def task_delete(request, pk):
    item = Task.objects.get(pk=pk)
    item.delete()
    messages.warning(request, 'Item Has Been Deleted')
    return redirect('home')


def cross_off(request, pk):
    item = Task.objects.get(pk=pk)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, pk):
    item = Task.objects.get(pk=pk)
    item.completed = False
    item.save()
    return redirect('home')


def task_edit(request, pk):
    if request.method == 'POST':
        item = Task.objects.get(pk=pk)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Has Been Edited!')
            return redirect('home')

    else:
        item = Task.objects.get(pk=pk)
        return render(request, 'edit.html', {'item': item})
