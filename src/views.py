from django.shortcuts import render
from django.core.cache import cache
from src.login import loginUser

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "user_page.html")

def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = loginUser(email, password)
    if user == None:
        return render(request, "index.html", {"failedToLogin": True})
    return user_page(request)

def user_page(request):
    return render(request, "user_page.html")