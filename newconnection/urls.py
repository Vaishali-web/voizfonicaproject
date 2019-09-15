from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('new/',views.conn, name="new"),
    path('approve/',views.approve, name="approve"),
    path("display/",views.displayhome,name="display"),
    url(r"^display/viewindividual$",views.individualfunction),

]