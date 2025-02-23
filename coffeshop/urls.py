"""
URL configuration for coffeshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from shop.views import home, menu, cart, CustomLoginView,product_detail, add_to_cart, checkout, register, cart_view, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', menu, name='menu'),  # Add this line
    path('cart/', cart, name='cart'),  # Cart Page
    path('checkout/', checkout, name='checkout'),  # Checkout URL
    path('register/', register, name='register'),  # Ensure this line exists
    path('login/', CustomLoginView.as_view(), name='login'),  # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
     path('cart/', cart_view, name='cart_view'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]

