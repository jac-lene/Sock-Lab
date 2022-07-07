from django.shortcuts import render, redirect
from .models import BasicSock
from .forms import SockForm
# Create your views here.

def sock_create(request):
    if request.method == 'POST':
        form = SockForm(request.POST)
        if form.is_valid():
            sock = form.save()
            return redirect('design-library/sock_detail', pk=sock.pk)
    else:
        form = SockForm()
    return render(request, 'sock-lab/sock_form.html', {'form': form})

def sock_edit(request, pk):
    sock = BasicSock.objects.get(pk=pk)
    if request.method == "POST":
        form = SockForm(request.POST, instance=sock)
        if form.is_valid():
            sock = form.save()
            return redirect('sock_detail', pk=sock.pk)
    else:
        form = SockForm(instance=sock)
    return render(request, 'sock-lab/sock_form.html', {'form': form})

def sock_list(request):
    socks = BasicSock.objects.all()
    return render(request, 'design-library/socks.html', {'socks': socks})

def sock_detail(request, pk):
    sock = BasicSock.objects.get(id=pk)
    return render(request, 'design-library/sock_detail.html', {'sock': sock})