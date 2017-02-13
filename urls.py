from django.conf.urls import url, include
from /home/puchto/djangoprojects/LAN1/LAN1/ import views.py

urlpatterns = [
    url(r'^$', views.clients_list, name='clients_list'),
]
