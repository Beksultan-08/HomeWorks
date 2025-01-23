from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('factorial/', views.factorial),
    path('info/', views.info),
    path('hello/', views.hello),
    path('sum/', views.sum),
    path('check/', views.check),
    path('filter/', views.filter),
    path('palindrome/', views.palindrome),
    path('age/', views.age),
    path('multiplication/', views.multiplication),
    path('max/', views.max),
    path('temp/', views.temp)
]