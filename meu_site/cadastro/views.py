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



def users_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        userlogin = authenticate(request, username = email, password= password)
        if userlogin:
            login(request, userlogin)
            return render(request, 'cadastro/site.html')
        else:
            context ={
                "erro" : 'Credenciais inválidas, verifique suas informações e tente novamente',
                'userlogin' : userlogin
            }
            return render(request, 'cadastro/login.html' , context)
    else:
        return render(request, 'cadastro/login.html' )



def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    if request.method == "POST":
        nome_completo = request.POST.get('nome_completo')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        
        user = User.objects.filter(email= email).first()
        if user:
            context = {
                'msg' : 'Email ja cadstrado, por favor, faça login com a conta vinculada a esse email',
                'user' : user
            }
            return render(request, 'cadastro/login.html', context)
        else:
            user = User.objects.create_user(username = nome_completo, password= senha, email = email)
            user.save()
        return render(request, 'cadastro/login.html', context)

    


