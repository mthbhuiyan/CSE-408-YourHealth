from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.generic.list import ListView

from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                address=form.cleaned_data['address'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude']
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        
        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
        url_is_safe = is_safe_url(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())

        if url_is_safe:
            return redirect(redirect_to)

        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


class OrderListView(ListView):
    template_name = 'orders/order/history.html'
    model = Order
