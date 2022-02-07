from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from rest_framework.request import Request
from mini_wallet.apps.wallets.models import WalletID


class TokenAuthentication(BaseAuthentication):
    """
    Wallet ID Token Authentication
    """

    def authenticate(self, request: Request) -> None:
        token = request.headers.get('Authorization')

        if not token:
            raise exceptions.AuthenticationFailed("Token not provided")

        if not WalletID.objects.filter(token=token).exists():
            raise exceptions.AuthenticationFailed("Invalid token")
