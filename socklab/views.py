from rest_framework import generics, permissions
from .serializers import SockSerializer
from .models import BasicSock
from .models import Stash
from .serializers import StashSerializer

class SockList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer

class SockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicSock.objects.all()
    serializer_class = SockSerializer

class StashList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Stash.objects.all()
    serializer_class = StashSerializer

class StashDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stash.objects.all()
    serializer_class = StashSerializer