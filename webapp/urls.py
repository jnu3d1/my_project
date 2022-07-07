from django.urls import path

from webapp.views import IndexView, create_task, TaskView, delete_task, edit_task, delete_multiple, MyRedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', create_task, name='create_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/delete/', delete_task, name='delete_task'),
    path('task/<int:pk>/editing/', edit_task, name='task_editing'),
    path('tasks/delete/', delete_multiple, name='delete_multiple'),
    path('weather/', MyRedirectView.as_view()),
]