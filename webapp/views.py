from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

# Create your views here.

from webapp.models import Task


def index(request):
    tasks = Task.objects.order_by('-status')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_date = request.POST.get('completion_date')
        if not completion_date:
            completion_date = None
        new_task = Task.objects.create(title=title, description=description, status=status,
                                       completion_date=completion_date)
        return redirect('task_view', pk=new_task.pk)


def task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    return render(request, 'task_view.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'task': task})
    task.delete()
    return redirect('index')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'edit.html', {'task': task})
    else:
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.completion_date = request.POST.get('completion_date')
        if not task.completion_date:
            task.completion_date = None
        task.save()
        return redirect('task_view', pk=task.pk)


def delete_multiple(request):
    if request.method == 'GET':
        tasks = Task.objects.order_by('-status')
        context = {'tasks': tasks}
        return render(request, 'delete_multiple.html', context)
    else:
        for pk in request.POST.getlist('checks[]'):
            task = get_object_or_404(Task, pk=pk)
            task.delete()
        return redirect('index')
