from django.shortcuts import render
from django.contrib.auth.views import LoginView
def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')  # Create this template


def cart(request):
    return render(request, 'cart.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Custom login template