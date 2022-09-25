from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('socks/', views.SockList.as_view(), name='sock_list'),
    path('socks/<int:pk>', views.SockDetail.as_view(), name='sock_detail'),
    path('stash/', views.StashList.as_view(), name='stash_list'),
    path('stash/<int:pk>', views.StashDetail.as_view(), name='stash_detail'),
]