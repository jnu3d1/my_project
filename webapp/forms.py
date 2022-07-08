from django import forms
from django.forms import widgets

from webapp.models import status_choices

class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок')
    description = forms.CharField(max_length=3000, label='Описание', widget=widgets.Textarea())
    status = forms.ChoiceField(choices=status_choices, label='Статус')
    completion_date = forms.DateField(required=False, label='Дата выполнения')