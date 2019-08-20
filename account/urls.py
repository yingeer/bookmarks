from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.shortcuts import render, redirect
from . import views as account_views


app_name = "account"

urlpatterns = [
    re_path(r"^$", account_views.dashboard, name="dashboard"),
    re_path(r"^register/$", account_views.user_register, name="user_register"),
    # re_path(r"^profile/$", account_views.show_profile, name="show_profile"),
    re_path(r"^profile/edit/$", account_views.edit_profile, name="edit_profile"),
]
