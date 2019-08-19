from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
    pass