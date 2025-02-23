from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .models import CartItem  # Assuming you have a CartItem model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Order
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')  # Create this template

# View Cart Page
# def cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

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

# Product Listing View
def menu(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})

# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Add to Cart View
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')



# def checkout(request):
#     return render(request, 'checkout.html') 

def checkout(request):
    if request.method == "POST":
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Coffee Order',
                            },
                            'unit_amount': int(request.POST.get("total_amount")) * 100,  # Convert to cents
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://127.0.0.1:8000/payment-success/',
                cancel_url='http://127.0.0.1:8000/payment-failed/',
            )

            # Save order to database
            order = Order.objects.create(user=request.user, total_amount=request.POST.get("total_amount"), payment_status="Pending")
            order.save()

            return JsonResponse({'sessionId': session.id})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, "checkout.html")

def payment_success(request):
    order = Order.objects.filter(user=request.user).latest('id')
    order.payment_status = "Paid"
    order.save()

    # Send confirmation email
    send_mail(
        "Order Confirmation",
        f"Dear {request.user.username},\n\nYour order has been successfully placed!\nOrder ID: {order.id}",
        "coffeeshop@example.com",
        [request.user.email],
        fail_silently=False,
    )

    return render(request, "payment_success.html", {"order": order})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1  # Increment quantity if already exists
        cart_item.save()
    
    return redirect('cart_view')  # Redirect to cart page

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')

