from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import PasswordChangeForm
from django.template.defaulttags import register
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from home.models import Magazine, UserProfile, Hashtag, MagazineIssue, DiscountCode
from home.forms import UserForm, UserProfileForm, UploadCodesFileForm, EmailChangeForm
from datetime import datetime
import random, string, secrets

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def is_mobile_device(request):
    # check visitor agent
    try:
        user_agent = request.META['HTTP_USER_AGENT']
    except:
        return False

    keywords = ['Mobile', 'Opera Mini', 'Android']

    if any(word in user_agent for word in keywords):
        return True
    else:
        return False


def home(request):
    ctx = {}

    ctx['magazines'] = Magazine.objects.all()

    if is_mobile_device(request):
        # mobile
        temp = 'mobiletemplates/homemobile.html'
    else:
        # desktop
        temp = 'home.html'

    return render(request, temp, context=ctx)


def user_login(request):
    # if HTTP POST pull relevant info
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home:home'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}.".format(username, password))
            return HttpResponse("Invalid login details supplied.")



    return render(request, "login.html", {})


def user_signup(request):
    registered = False

    if is_mobile_device(request):
        # mobile
        temp = 'mobiletemplates/signupmobile.html'
    else:
        # desktop
        temp = 'signup.html'

    # if HTTP POST then process form
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        profile_form = UserProfileForm(data=request.POST)

        # if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
            return render(request, temp, {'form': user_form})
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    ctx = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}



    return render(request, temp, context=ctx)


@login_required
def my_profile(request):
    ctx= {}
    password_form = PasswordChangeForm(request.user,prefix='password_form')
    email_form = EmailChangeForm(request.user, prefix='email_form')
    user = UserProfile.objects.get(user=request.user)
    issues = user.saved_issues.order_by("magazine")

    ctx['magazines'] = Magazine.objects.all()
    ctx['savedissues'] = issues.all()

    if request.method == 'GET':
        email_form = EmailChangeForm(request.user,initial={'new_email1': request.user.email})

    if request.method == 'POST':
        action = request.POST['action']

        if action == 'edit_email':
            email_form = EmailChangeForm(request.user, request.POST)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, 'Email updated')
                return redirect(reverse('home:myprofile'))

        if action == 'edit_password':
            password_form = PasswordChangeForm(request.user, request.POST, prefix='password_form')
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated')
                return redirect(reverse('home:myprofile'))



    ctx['email_form'] = email_form
    ctx['password_form'] = password_form

    if is_mobile_device(request):
        # mobile
        temp = 'mobiletemplates/membershipmenumobile.html'
    else:
        # desktop
        temp = 'myprofile.html'

    return render(request, temp, ctx)



def membership(request):
    ctx = {}
    ctx['magazines'] = Magazine.objects.all()

    if request.user.is_authenticated:
        ctx['subscribed'] = UserProfile.objects.get(user=request.user).is_subscribed
 

    return render(request, 'membership.html', context=ctx)   


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
    ctx['latest_issue'] = MagazineIssue.objects.filter(magazine=mag).first()

    if is_mobile_device(request):
        temp = 'mobiletemplates/magazinemobile.html'
    else:
        temp = 'magazine.html'

    return render(request, temp, context=ctx)



def issue(request, id, slug):
    ctx = {}

    mag = Magazine.objects.get(id=id)
    issue = MagazineIssue.objects.get(slug=slug)

    ctx['this'] = mag
    ctx['thisIssue'] = issue
    ctx['magazines'] = Magazine.objects.all()
    ctx['issues'] = MagazineIssue.objects.filter(magazine=mag)

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        ctx['saved_issues'] = user.saved_issues.all()
        ctx['subscribed'] = UserProfile.objects.get(user=request.user).is_subscribed

    if is_mobile_device(request):
        temp = 'mobiletemplates/issuemobile.html'
    else:
        temp = 'issue.html'

    return render(request, temp, context=ctx)


@login_required
def mymags(request):
    ctx = {}

    user = UserProfile.objects.get(user=request.user)
    issues = user.saved_issues.order_by("magazine")

    ctx['magazines'] = Magazine.objects.all()
    ctx['savedissues'] = issues.all()

    return render(request, 'mymagazines.html', context=ctx)


@login_required
def save_issue(request):
    if request.method == 'POST':
        issue_name = request.POST.get('name')

        issue = MagazineIssue.objects.get(slug=issue_name)
        user = UserProfile.objects.get(user=request.user)

        for i in user.saved_issues.all():
            # This removes attraction from the list if already present hence acting as a toggle
            if i == issue:
                user.saved_issues.remove(issue)
                user.save()
                return JsonResponse({'success': 'true', 'value': 0})

        user.saved_issues.add(issue)
        user.save()

        return JsonResponse({'success': 'true', 'value': 1})

    return JsonResponse({'success': 'false'})


def contact(request):
    ctx = {}

    ctx['magazines'] = Magazine.objects.all()

    return render(request, 'contact.html', context=ctx)


@staff_member_required
def staff(request):
    ctx = {}

    ctx['magazines'] = Magazine.objects.all()

    return render(request, 'staff.html', context=ctx)


@staff_member_required
def codes(request):
    ctx = {}
    ctx['magazines'] = Magazine.objects.all()
    ctx['codefile'] = None

    form = UploadCodesFileForm()

    if request.method == 'POST':
        form = UploadCodesFileForm(request.POST)
        
        if form.is_valid():
            time, codes = gen_codes(request.POST.get("amount"))
            ctx['codefile'] = time
               
            #Delete all existing codes from database for now... (this will need to change for release)
            DiscountCode.objects.all().delete()

            #Save codes to DB
            for code in codes:
                code = code[:-1]
                new_code = DiscountCode(code=code)
                new_code.save()

    ctx['range'] = range(5,501,5)
    ctx['form'] = form
    ctx['errors'] = form.errors or None


    return render(request, 'codes.html', context=ctx)


def gen_codes(amount):
    time = datetime.now().strftime("%d-%m-%Y %H%M%S")
    path = 'static/code_templates/' + time + '.csv'
    codes = []
    code_length = 16

    with open(path, 'w+') as f:
        for i in range(int(amount)):
            #---This line of code has come from https://www.javatpoint.com/python-program-to-generate-a-random-string
            code = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(code_length)) + ','
            f.write(code)
            codes.append(code)
        
    return path, codes


@login_required
def send_email(request):
    user = UserProfile.objects.get(user=request.user)

    if user.is_subscribed == False:
        return HttpResponse("Sorry, you are not a subscriber!")
    
    try:
        code = DiscountCode.objects.all()[0]
    except IndexError:
        return HttpResponse("There are no available codes at the moment. If you think there should be, please get in touch.")


    text = """
    Hey """ + request.user.username + """,


    Thank you so much for making the decision to subscribe to Clò this month. Here is your unique discount code which 
    can be used once across any of the magazines on our site marked with a 'subscriber price'.

    Please ensure to keep this email or your code safe as it cannot be resent.

    """ + code.code + """


    The Clò Team. """


    email = EmailMessage(
        subject = 'Your unique Clò discount code',
        body = text,
        from_email = 'clo.magazines@gmail.com',
        to = [request.user.email],
        )

    try:
       email.send()
    except Exception as e:
        print(e)
        return HttpResponse("Oops! Something went wrong.")

    code.delete()

    return HttpResponseRedirect(reverse('home:membership'))