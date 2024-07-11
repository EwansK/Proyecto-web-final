from django.urls import path
from .views import home_view, products_view, about_view, register_view, login_view, profile_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('products/', products_view, name='products'), 
    path('about/', about_view, name='about'), 
    path('register/', register_view, name='register'), 
    path('login/', login_view, name='login'), 
    path('profile', profile_view, name='profile'), 

] 