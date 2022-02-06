from . import views
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('uploaded/', views.uploaded, name='uploaded')
]