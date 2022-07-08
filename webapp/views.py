from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, RedirectView

from forms import TaskForm
from webapp.models import Task


class IndexView(View):
    def get(self, request):
        tasks = Task.objects.order_by('-status')
        context = {'tasks': tasks}
        return render(request, 'index.html', context)


def create_task(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            completion_date = form.cleaned_data.get('completion_date')
            # if not completion_date:
            #     completion_date = None
            new_task = Task.objects.create(title=title, description=description, status=status,
                                           completion_date=completion_date)
            return redirect('task_view', pk=new_task.pk)
        return render(request, 'create.html', {'form': form})


class TaskView(TemplateView):
    template_name = 'task_view.html'

    # def get_template_names(self):
    #     return 'task_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


# def task_view(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return HttpResponseNotFound('<h1>Страница не найдена</h1>')
#     return render(request, 'task_view.html', {'task': task})


class MyRedirectView(RedirectView):
    url = "https://p.ya.ru/bishkek"


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'task': task})
    task.delete()
    return redirect('index')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'completion_date': task.completion_date
        })
        return render(request, 'edit.html', {'form ': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.completion_date = form.cleaned_data.get('completion_date')
            # if not task.completion_date:
            #     task.completion_date = None
            task.save()
            return redirect('task_view', pk=task.pk)
        return render(request, 'edit.html', {'form': form})


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
