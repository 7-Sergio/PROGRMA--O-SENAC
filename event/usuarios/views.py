from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'GET':
        return render(request,'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        nomeCompleto = request.POST.get('NomeCompleto')
        celular = request.POST.get('Celular')
        email = request.POST.get('email')
        senha = request.POST.get('Senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        
        if not(senha == confirmar_senha):
            return redirect(reverse('cadastro'))
        
        
        user = User.objects.filter(username=username)
        
        
        if user.exists():
            return redirect(reverse('cadastro'))
        
        
        user = User.objects.create_user(username=username,nomeCompleto=nomeCompleto,celular=celular,email=email,senha=senha,password=senha)
        
        user.save()
        return redirect(reverse('login'))
        
        