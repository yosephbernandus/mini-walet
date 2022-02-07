from django.urls import path

from .views import Login

app_name = "init"

urlpatterns = [
    path('', Login.as_view(), name="login"),
]
