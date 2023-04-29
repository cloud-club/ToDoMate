from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('test',main),
    path('month/<int:month>/',findMonth),
    path('day/',findDay),
]
