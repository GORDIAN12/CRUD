from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


@login_required
def clients(request):
    clientes=Cliente.objects.all()
    return render(request, 'clients/index.html', {'clientes': clientes})

def exit(request):
    logout(request)
    return redirect('/accounts/login')
def create(request):
    form=ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clients')
    return render(request, 'clients/create.html', {'form': form})

def edit(request, id):
    cliente=Cliente.objects.get(id=id)
    form=ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('clients')
    return render(request, 'clients/edit.html', {'form': form})

def delete(request, id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clients')

