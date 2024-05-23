# Importing required libraries
from django.urls import pathf
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about.html',views.about,name="about"),
]
