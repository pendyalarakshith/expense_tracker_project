from django.urls import path
from . import views
from .models import Category
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
]
