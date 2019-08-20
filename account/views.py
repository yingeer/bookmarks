from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm, RegisterForm, ProfileForm, UserEditForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.


def user_login(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get("username", "")
            password = cd.get("password", "")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:                        
                    login(request, user)   # 集成当前用户到session中                     
                    return HttpResponse('Authenticated successfully')
                else:                        
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    context['form'] = form # form.errors
    return render(request, "account/login.html", context)

# login logout login and logout

@login_required  
def dashboard(request):
    context = {}
    context['section'] = "dashboard"
    """在用户登入后"""
    return render(request, "account/dashboard.html", context)


def user_register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password2'])
            if cd['first_name']:
                last_name = cd['username'] - cd['first_name']
                new_user.last_name = last_name
            else:
                new_user.first_name = ""
                new_user.last_name = cd['username']
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.save()
    elif request.method == "GET":
        form = RegisterForm()
    context['form'] = form

    return render(request, "registration/register.html", context)

@login_required
def edit_profile(request):
    context = {}
    if request.method == "POST":
        user_edit_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, 
                                    instance=request.user.profile,
                                    files=request.FILES)
        profile = ProfileForm()
        if user_edit_form.is_valid() and profile_form.is_valid():
            user_edit_form.save()
            profile_form.save()
    elif request.method == "GET":
        user_edit_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context["user_edit_form"] = user_edit_form
    context['profile_form'] = profile_form
    return render(request, 'account/profile_edit.html', context)

