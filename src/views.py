from django.shortcuts import render
from django.core.cache import cache
from src.user_access import loginUser, registerUser, getActiveUser

def index(request):
    return render(request, "index.html")

def user_page(request, user):
    return render(request, "user_page.html", {"user": user})

def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(request.POST)
    user = registerUser(name, email, password)
    print(user)
    if user == None:
        return render(request, "index.html", {"failedToRegister": True})
    return user_page(request, user)

def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = loginUser(email, password)
    if user == None:
        return render(request, "index.html", {"failedToLogin": True})
    
    print("successfully logined user"); 

    return user_page(request, user)

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_POST
def start_task(request):
    # Для JSON-данных
    data = json.loads(request.body)
    print(data)  # {'key': 'value'}

    # Для FormData (обычные POST-данные)
    # name = request.POST.get('name')

    return JsonResponse({'status': 'success'})

    print(request.POST)
    user = getActiveUser();
    return render(request, "task.html", {"user": user})
