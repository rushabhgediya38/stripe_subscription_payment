from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('config/', views.stripe_config, name='config'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session/'),
    path('create-ultimate-checkout-session/', views.create_ultimate_checkout_session,
         name='create-ultimate-checkout-session/'),
    path('success/', views.success, name='success'),
    path('pricing/', views.pricing_details, name='pricing'),
    path('cancel/', views.cancel, name='cancel-subscription'),
    path('webhook/', views.stripe_webhook),
]
