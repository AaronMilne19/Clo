from django.shortcuts import render, redirect
from home.models import Magazine, UserProfile


def home(request):
    ctx = {}
    
    ctx['magazines'] = Magazine.objects.all()

    return render(request, 'home.html', context=ctx)


def login(request):
    ctx = {}

    return render(request, 'login.html', context=ctx)


def signup(request):
    ctx = {}

    return render(request, 'signup.html', context=ctx)


def magazine(request, id):
    ctx = {}

    ctx['this'] = Magazine.objects.get(id=id)
    ctx['magazines'] = Magazine.objects.all()

    return render(request, 'magazine.html', context=ctx)