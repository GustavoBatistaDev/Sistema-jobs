from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não conferem.')
            return redirect('/auth/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Nenhum campo pode ser nulo.')
            return redirect('/auth/cadastro')
            
        user = User.objects.filter(username=username)

        if len(user) > 0:
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('/auth/cadastro')
      
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso. faça login.')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema. Tente novamente.')
            return redirect('/auth/cadastro')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)

    if not usuario:
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
        return redirect('login')
    else:
        auth.login(request, usuario)
        return redirect('/jobs/encontrar_jobs')

def sair(request):
    auth.logout(request)
    return redirect('/auth/login')