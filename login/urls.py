from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('resetpass/', views.resetpass, name="resetpass"),
    
]