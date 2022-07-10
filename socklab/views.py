from rest_framework import generics, permissions
from .serializers import SockSerializer
from .models import BasicSock

class SockList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer

class SockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer