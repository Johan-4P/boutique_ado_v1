from django.urls import path 
from . import views
from .webhooks import stripe_webhook  # Import stripe_webhook from webhooks

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', stripe_webhook, name='stripe_webhook'),  # Use the correct import
]
