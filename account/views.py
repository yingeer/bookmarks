from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm
from django.http import HttpResponse
# Create your views here.

def user_login(request):
    pass