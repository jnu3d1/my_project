from django.urls import path

from webapp.views import index, create_task, task_view, delete_task, edit_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/add/', create_task, name='create_task'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('tasks/delete/', delete_task, name='delete_task'),
    path('task/<int:pk>/editing', edit_task, name='task_editing')
]