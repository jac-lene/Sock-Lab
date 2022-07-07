from django.urls import path
from . import views

urlpatterns = [
    path('', views.sock_list, name='sock_list'),
    # tunr/urls.py
    path('socks/<int:pk>', views.sock_detail, name='sock_detail'),
    path('sock-lab/new', views.sock_create, name='sock_create'),
    path('socks/<int:pk>/edit', views.sock_edit, name='sock_edit'),
    path('socks/<int:pk>/delete', views.sock_delete, name='sock_delete'),
]