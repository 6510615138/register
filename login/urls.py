
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('login',views.getUsername),
    path('logout',views.user_logout)
]