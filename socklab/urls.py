from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('socks/', views.SockList.as_view(), name='sock_list'),
    path('socks/<int:pk>', views.SockDetail.as_view(), name='sock_detail'),
]