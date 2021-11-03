from django.shortcuts import render, redirect


def home(request):
    ctx = {}
    
    return render(request, 'home.html', context=ctx)