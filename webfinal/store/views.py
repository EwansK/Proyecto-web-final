from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html', {})

def products_view(request):
    return render(request, 'products.html', {})

def about_view(request):
    return render(request, 'about.html', {})

def register_view(request):
    return render(request, 'register.html', {})

def login_view(request):
    return render(request, 'login.html', {})

def profile_view(request):
    return render(request, 'profile.html', {})