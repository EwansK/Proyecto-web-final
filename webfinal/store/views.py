from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Customer, User, Product, Category
from .forms import CustomerCreationForm, CustomerUpdateForm
from django.contrib.auth.models import User

#Home
def home_view(request):
    return render(request, 'home.html', {})

#Productos
def products_view(request):
    product_list = Product.objects.order_by('id')
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id and category_id != '0': 
        try:
            category_id = int(category_id)
            product_list = product_list.filter(category_id=category_id)
        except ValueError:
            pass

    paginator = Paginator(product_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'categories': categories,
        'selected_category': category_id if category_id and category_id != '0' else None,
    }

    return render(request, 'products.html', context)


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)

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
@login_required
def profile_view(request):
    user = request.user
    customer = user.customer
    context = {
        'user': user,
        'customer': customer,
    }
    return render(request, 'profile.html', context)

#Actualizar info
@login_required
def edit_profile_view(request):
    user = request.user
    customer = user.customer

    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Información actualizada correctamente!')
            return redirect('profile')
    else:
        form = CustomerUpdateForm(instance=customer)

    return render(request, 'edit_profile.html', {'form': form})

#Eliminar usuario
@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Su cuenta ha sido eliminada de nuestros sistemas, hasta pronto.')
        return redirect('home') 
    return render(request, 'confirm_delete.html')

#Cierre de sesión
def logout_view(request):
    logout(request)
    messages.success(request, ('Sesión finalizada.'))
    return redirect('home')
    