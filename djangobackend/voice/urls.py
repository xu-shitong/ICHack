from . import views
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('',views.index, name='index')
]