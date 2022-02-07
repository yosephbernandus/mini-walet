from django.conf.urls import include
from django.urls import path

app_name = "api"

urlpatterns = [
    path('init/', include('mini_wallet.api.init.urls', namespace='init')),
]
