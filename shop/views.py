from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .models import CartItem  # Assuming you have a CartItem model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')  # Create this template


def cart(request):
    return render(request, 'cart.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Custom login template
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def checkout(request):
    return render(request, 'checkout.html') 
    
# def checkout(request):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirects to login if the user is not authenticated

#     cart_items = CartItem.objects.filter(user=request.user)
#     cart_total = sum(item.total for item in cart_items)

#     return render(request, 'checkout.html', {'cart_items': cart_items, 'cart_total': cart_total})