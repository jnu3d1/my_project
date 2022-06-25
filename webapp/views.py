from django.shortcuts import render

# Create your views here.

from webapp.models import Task

def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_date = request.POST.get('completion_date')
        new_task = Task.objects.create(description=description, status=status, completion_date=completion_date)
        context = {'task': new_task}
        return render(request, 'task_view.html', context)

def task_view(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    return render(request, 'task_view.html', {'task': task})

def delete_task(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    removal = task.delete()
    return render(request, 'index.html', {'action': removal})