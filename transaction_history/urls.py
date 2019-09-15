from django.conf.urls import url
from transaction_history import views

urlpatterns = [
    url('', views.getTransactions,name="transactions"),  #http :8000/plans/ in a new terminal  # in browser 127.0.0.1:8000/plans/
   
]