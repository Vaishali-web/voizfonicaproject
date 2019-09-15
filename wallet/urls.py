from django.conf.urls import url
from wallet import views

urlpatterns = [
    url(r'', views.getWallet),
      
]