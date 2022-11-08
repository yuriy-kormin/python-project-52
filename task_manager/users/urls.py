from django.urls import path
from .views import  UserListView
from django.contrib import admin

urlpatterns = [
    path('', UserListView.as_view())
]
