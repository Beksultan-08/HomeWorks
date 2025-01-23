from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('factorial/', views.factorial),
    path('info/', views.info),
    path('hello/', views.hello),
    path('sum/', views.sum),
    path('check/', views.check),
    path('filter/', views.filter)
]