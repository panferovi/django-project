from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from dataclasses import asdict
from src.user_access import loginUser, registerUser, getActiveStats, updateActiveStats
import json

def index(request):
    return render(request, "index.html")

def user_page(request, user):
    return render(request, "user_page.html", {"user": user})

def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = registerUser(name, email, password)
    if user == None:
        return render(request, "index.html", {"failedToRegister": True})
    return user_page(request, user)

def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = loginUser(email, password)
    if user == None:
        return render(request, "index.html", {"failedToLogin": True})
    

    return user_page(request, user)

def init_stats(request):
    return JsonResponse(asdict(getActiveStats()))

def update_stats(request):
    data = json.loads(request.body)
    stats = updateActiveStats(data['isCorrect'], data['currentTopic'])    
    return JsonResponse(asdict(stats))