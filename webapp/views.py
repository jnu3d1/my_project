from django.shortcuts import render

# Create your views here.

from webapp.models import Task

def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def create_task(request):
    pass

def task_view(request):
    pass