from django.shortcuts import render
from .models import BasicSock

# Create your views here.

def sock_list(request):
    socks = BasicSock.objects.all()
    return render(request, 'design-library/socks.html', {'socks': socks})

def sock_detail(request, pk):
    sock = BasicSock.objects.get(id=pk)
    return render(request, 'design-library/sock_detail.html', {'sock': sock})