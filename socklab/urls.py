from django.urls import path
from . import views

urlpatterns = [
    path('', views.sock_list, name='sock_list'),
    # tunr/urls.py
    path('socks/<int:pk>', views.sock_detail, name='sock_detail'),
    path('sock-lab/new', views.sock_create, name='sock_create'),
]