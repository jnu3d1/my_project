from django.urls import path

from webapp.views import index, create_task, task_view

urlpatterns = [
    path('', index),
    path('tasks/add/', create_task),
    path('tasks/', task_view),
]