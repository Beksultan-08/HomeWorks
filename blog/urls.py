from django.urls import path
from . import views

urlpatterns = [
    path('factorial/', views.factorial),
    path('info/', views.info),
    path('task-1/', views.task_1),
    path('task-7/', views.task_7),
]