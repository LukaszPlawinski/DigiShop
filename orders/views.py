from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET

def order_create(request):
    cart = Cart(request)
    total = int(cart.get_total_price() * 100)
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
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
            return render(request,
                            'created.html',
                            {'order': order})
    else:
        form = OrderCreateForm()
        key = settings.STRIPE_PUBLISHABLE
    return render(request,
                'create.html',
                {'cart': cart, 'form': form, 'key':key, 'total':total})
                