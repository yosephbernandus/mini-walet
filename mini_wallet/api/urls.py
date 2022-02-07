from django.conf.urls import include
from django.urls import path

app_name = "api"

urlpatterns = [
    path('init/', include('mini_wallet.api.init.urls', namespace='init')),
    path('wallet/', include('mini_wallet.api.wallet.urls', namespace='wallet')),
]
