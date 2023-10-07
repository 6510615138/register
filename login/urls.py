
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.getUsername),
    path('logout',views.user_logout)
]