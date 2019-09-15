
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getUser/', views.getUser, name="getUser"),
    path('doRegister/', views.doRegister, name="doRegister"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('usageSimulator/',views.usageSimulator,name="usageSimulator")
]
