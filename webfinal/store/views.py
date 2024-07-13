from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer
from .forms import CustomerCreationForm
from django.contrib.auth.models import User

#Home
def home_view(request):
    return render(request, 'home.html', {})

#Productos
def products_view(request):
    return render(request, 'products.html', {})

#Info de la empresa
def about_view(request):
    return render(request, 'about.html', {})

#Registro
def register_view(request):
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro completado exitosamente!')
            return redirect('home')
        else:
            messages.error(request, 'Registro fallido, intente nuevamente.')
    else:
        form = CustomerCreationForm()

    return render(request, 'register.html', {'form': form})
    
#Iniciar sesión
def login_view(request):
    if request.method == "POST":
        email = request.POST['email1']
        password = request.POST['password1']
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Sesión iniciada correctamente!'))
            return redirect('home')
        else:        
            messages.error(request, ('Inicio de sesión fallido, intente nuevamente.'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

#Perfil de usuario
def profile_view(request):
    return render(request, 'profile.html', {})

#Cierre de sesión
def logout_view(request):
    logout(request)
    messages.success(request, ('Sesión finalizada.'))
    return redirect('home')
    