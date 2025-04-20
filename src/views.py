"""Module allows to render pages using Django api"""

from django.shortcuts import render
from django.http import JsonResponse
from dataclasses import asdict
from src.user_access import login_user, register_user, get_active_stats, update_active_stats
import json


def index(request):
    """Function renders index page"""
    return render(request, "index.html")


def user_page(request, user):
    """Function renders user page"""
    return render(request, "user_page.html", {"user": user})


def register(request):
    """Function tries to register user and render user page"""
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = register_user(name, email, password)
    if user is None:
        return render(request, "index.html", {"failedToRegister": True})
    return user_page(request, user)


def login(request):
    """Function tries to login user and render user page"""
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = login_user(email, password)
    if user is None:
        return render(request, "index.html", {"failedToLogin": True})

    return user_page(request, user)


def init_stats(_):
    """Function inits active user stats on the local machine"""
    return JsonResponse(asdict(get_active_stats()))


def update_stats(request):
    """Function updates active user stats on the server"""
    data = json.loads(request.body)
    stats = update_active_stats(data["is_correct"], data["currentTopic"])
    return JsonResponse(asdict(stats))
