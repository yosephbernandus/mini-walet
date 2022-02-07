from django.urls import path

from .views import Wallet

app_name = "wallet"

urlpatterns = [
    path('', Wallet.as_view(), name="wallet"),
]
