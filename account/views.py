from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def user_active_action(request, user):
    if user.is_active:                        
        login(request, user)                        
        return HttpResponse('Authenticated successfully')
    else:                        
        return HttpResponse('Disabled account')

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
                user_active_action(request, user)
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, "account/login.html", context)