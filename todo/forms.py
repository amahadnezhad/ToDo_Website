from django import forms

from .models import Task


class ListForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['item', 'completed']
