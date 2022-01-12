from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from home.models import Magazine, UserProfile, Hashtag, MagazineIssue
from home.forms import UserForm, UserProfileForm
from django.template.defaulttags import register



def home(request):
    ctx = {}
    
    ctx['magazines'] = Magazine.objects.all()


    return render(request, 'home.html', context=ctx)


def user_login(request):
    #if HTTP POST pull relevant info
    if request.method=='POST':
    	username=request.POST.get('username')
    	password=request.POST.get('password')
    	user=authenticate(username=username,password=password)
    	
    	if user:
    		if user.is_active:
    			login(request, user)
    			return HttpResponseRedirect(reverse('home:home'))
    		else:
    			return HttpResponse("Your account is disabled")
    	else:
    		print("Invalid login details: {0}, {1}.".format(username,password))
    		return HttpResponse("Invalid login details supplied.")
    else:
    	return render(request, 'login.html', {})

    


def user_signup(request):
    registered=False
    
    #if HTTP POST then process form
    if request.method=='POST':
    	user_form=UserForm(data=request.POST)

    	profile_form=UserProfileForm(data=request.POST)
    	
    	#if both forms are valid
    	if user_form.is_valid() and profile_form.is_valid():
    		user=user_form.save(commit=False)
    		user.set_password(user.password)
    		user.save()
    		
    		profile=profile_form.save(commit=False)
    		profile.user=user
    		profile.save()
    		
    		registered=True
    	else:
    		print(user_form.errors, profile_form.errors)
    		return render(request,'signup.html', {'form':user_form})
    else:
    	user_form=UserForm()
    	profile_form=UserProfileForm()
    		
    ctx = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}

    return render(request, 'signup.html', context=ctx)

@login_required
def user_signout(request):
	logout(request)
	return redirect(reverse('home:home'))



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
