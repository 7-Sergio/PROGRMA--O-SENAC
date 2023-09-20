from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'GET':
        return render(request,'cadastro.html')