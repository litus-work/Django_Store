from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    form = OrderCreateForm(request.POST or None)
    cart = Cart(request)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            user=request.user,
            city=form.cleaned_data['city'],
            warehouse=form.cleaned_data['warehouse'],
            total_price=cart.get_total_price(),
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price'],
            )
        cart.clear()
        return render(request, 'orders/created.html', {'order': order})

    return render(request, 'orders/create.html', {'form': form, 'cart': cart})

