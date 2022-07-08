from rest_framework import generics
from .serializers import SockSerializer
from .models import BasicSock

class SockList(generics.ListCreateAPIView):
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer

class SockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer