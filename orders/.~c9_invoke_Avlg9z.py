from django.shortcuts import render,redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
import stripe
from shop.models import Category
from django.contrib.auth.decorators import login_required

#Importing stripe key
stripe.api_key = settings.STRIPE_SECRET


'''
Function is responsible for creating the order and payment
'''
@login_required(login_url='/accounts/login')
def order_create(request):
    cart = Cart(request)
#Multiply total price for stripe
    total = float(cart.get_total_price() * 100)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.total = cart.get_total_price()
            order.save()
#Stripe payment details
            charge = stripe.Charge.create(
                amount= total,
                currency='EUR',
                description= order.id,
                source=request.POST['stripeToken']
        )
        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return redirect('orders:my_order')
    else:
        form = OrderCreateForm()
        key = settings.STRIPE_PUBLISHABLE
    return render(request,
                'create.html',
                {'cart': cart, 'form': form, 'key':key, 'total':total, 'categories': categories})


def my_order(request):
    categories = Category.objects.all()
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders':orders, 'categories': categories})