from django.shortcuts import render, redirect
from home.models import Magazine, UserProfile, Hashtag, MagazineIssue


def home(request):
    ctx = {}
    
    ctx['magazines'] = Magazine.objects.all()
    ctx['hashtags'] = Hashtag.objects.all()

    return render(request, 'home.html', context=ctx)


def login(request):
    ctx = {}

    return render(request, 'login.html', context=ctx)


def signup(request):
    ctx = {}

    return render(request, 'signup.html', context=ctx)
    

def myprofile(request):
    ctx = {}

    return render(request, 'myprofile.html', context=ctx)


def magazine(request, id):
    ctx = {}

    mag = Magazine.objects.get(id=id)

    ctx['this'] = mag
    ctx['magazines'] = Magazine.objects.all()
    ctx['issues'] = MagazineIssue.objects.filter(magazine=mag)

    return render(request, 'magazine.html', context=ctx)
