from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    ctx = {}
    
    return render(request, 'home.html', context=ctx)