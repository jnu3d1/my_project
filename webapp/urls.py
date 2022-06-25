from django.urls import path

from webapp.views import index, create_task, task_view

urlpatterns = [
    path('', index),
    path('task/add/', create_task),
    path('task/', task_view),
]