from django.urls import path

from webapp.views import index, create_task, task_view, delete_task

urlpatterns = [
    path('', index),
    path('tasks/add/', create_task),
    path('task/', task_view),
    path('tasks/delete/', delete_task),
]