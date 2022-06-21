from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('delete/<int:id>', views.delete, name="delete"),
]