from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()  # Ensure this form includes all required fields
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R95nuQ9dggv1ihREcc5MSEa6dWyyMWiEsPmvj5L9wm4C86efeouET9AAAcFpIkoN7fSbwATsIcvpHSlZ3zg288b0083HaP5ma',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)


