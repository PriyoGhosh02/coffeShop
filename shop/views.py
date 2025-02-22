from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .models import CartItem  # Assuming you have a CartItem model

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')  # Create this template


def cart(request):
    return render(request, 'cart.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Custom login template
    
    
# def checkout(request):
#     # Check if user is logged in (if using authentication)
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect to login page if not logged in

#     # Get cart items for the logged-in user
#     cart_items = CartItem.objects.filter(user=request.user)
    
#     # Calculate total price
#     cart_total = sum(item.total for item in cart_items)

#     return render(request, 'checkout.html', {'cart_items': cart_items, 'cart_total': cart_total})

def checkout(request):
    # Assuming you have a cart system and CartItem model that tracks the user's cart
    cart_items = CartItem.objects.filter(user=request.user)  # Get cart items for the logged-in user
    cart_total = sum(item.total for item in cart_items)  # Calculate the total price of the cart items
    
    # If the request method is POST, we can process the checkout (e.g., payment logic)
    if request.method == 'POST':
        # You can process the order here (e.g., save to the database, create order, etc.)
        return HttpResponse("Order successfully placed!")
    
    # Render the checkout page with cart items and the total
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })
