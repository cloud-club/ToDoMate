from django.contrib import admin
from django.urls import path
from .views import main
urlpatterns = [
    path(''),
    path('test',main),
    path('month/<int:month>/'),
    path('day/'),
    path('<int:pk>/'),
]
