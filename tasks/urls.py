from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task_list_create'),
    path('tasks/<str:pk>/',TaskDetail.as_view(), name='task_detail'),
]
