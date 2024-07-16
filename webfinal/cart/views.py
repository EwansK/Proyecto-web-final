from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart =Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantity
    total= cart.cart_total()
    context = {"cart_products": cart_products, "quantities": quantities, "total": total}
    return render(request, "cart_summary.html", context)

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})
        messages.success(request, '¡Producto añadido al carro de compras!')
        return response


    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        messages.success(request, 'Producto eliminado.')
        response = JsonResponse({'product':product_id})
    return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity= product_qty)
        messages.success(request, 'Cantidad actualizada.')
        response = JsonResponse({'qty':product_qty})
    return response