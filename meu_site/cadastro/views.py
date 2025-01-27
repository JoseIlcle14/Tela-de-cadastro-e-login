from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.



def site(request):
    if request.user.is_authenticated():
        return render(request, 'cadastro/site.html')
    else:
        return HttpResponse("falha de login")





def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    if request.method == "POST":
        nome_completo = request.POST.get('nome_completo')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        
        user = User.objects.filter(email= email).first()
        if user:
            return HttpResponse("E-mail já cadastrado. Tente outro.")
        
        user = User.objects.create_user(username = nome_completo, password= senha, email = email)
        user.save()
        return HttpResponse("cadastrado com sucesso")
    


def users_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username = email, password= password)
        if user:
            login(request, user)
            return render(request, 'cadastro/site.html')
        else:
            return HttpResponse(f"credenciais inválidas ")
    else:
        return render(request, 'cadastro/login.html' )

