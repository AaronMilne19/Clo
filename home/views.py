from django.shortcuts import render, redirect
from home.models import Magazine, UserProfile, Hashtag, MagazineIssue
from django.contrib.auth.decorators import login_required


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

    mag = Magazine.objects.get(id=id)

    ctx['this'] = mag
    ctx['magazines'] = Magazine.objects.all()
    ctx['issues'] = MagazineIssue.objects.filter(magazine=mag)


    return render(request, 'magazine.html', context=ctx)


def issue(request, id, slug):
    ctx = {}

    mag = Magazine.objects.get(id=id)
    issue = MagazineIssue.objects.get(slug=slug)

    ctx['this'] = mag
    ctx['thisIssue'] = issue
    ctx['magazines'] = Magazine.objects.all()
    ctx['issues'] = MagazineIssue.objects.filter(magazine=mag)

    return render(request, 'issue.html', context=ctx)


@login_required
def mymags(request):
    ctx = {}

    #user = UserProfile.objects.get(user=request.user)
    

    ctx['magazines'] = Magazine.objects.all()
    ctx['savedissues'] = MagazineIssue.objects.all() #This will change

    return render(request, 'mymagazines.html', context=ctx)
