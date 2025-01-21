from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import UsuariosCadastrados
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def tabela(request):
    users = UsuariosCadastrados.objects.all() 
    context = {
        'usuarios': users
    }
    return render(request, 'cadastro/tabela.html', context)

def users_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username = email, passoword= senha)
        if user is not None:
            login(request, user)
            return redirect('/site/')
        else:
            return HttpResponse("credenciais inválidas")

    return render(request, 'cadastro/login.html' )


def site(request):
    return render(request, 'cadastro/site.html')






def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    if request.method == "POST":
        nome_completo = request.POST.get('nome_completo')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        if UsuariosCadastrados.objects.filter(email = email).exists():
            return HttpResponse("E-mail já cadastrado. Tente outro.")
        else:
            UsuariosCadastrados.objects.create(nome_completo = nome_completo, senha = senha, email = email)
            return redirect('/tabela/')
    
