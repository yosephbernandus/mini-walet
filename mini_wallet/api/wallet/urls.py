from django.urls import path

from .views import Wallet, Deposit

app_name = "wallet"

urlpatterns = [
    path('', Wallet.as_view(), name="wallet"),
    path('deposits', Deposit.as_view(), name="deposits"),
]
