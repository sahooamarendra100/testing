from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('update/<int:id>', views.update, name="update"),
    
    path('update_employee/', views.update_employee, name="update_employee"),
]