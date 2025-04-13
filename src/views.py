from django.shortcuts import render
from django.core.cache import cache

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "user_page.html")

def login(request):
    email = request.POST.get("email")
    print(email);


    context = {"failedToLogin": True}
    iiii = 0;
    if iiii % 2:
        iiii += 1;
        context.failedToLogin = True;
    return render(request, "index.html", context)

def user_page(request):
    return render(request, "user_page.html")