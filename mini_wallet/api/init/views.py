from django.shortcuts import get_object_or_404
from mini_wallet.api.views import WalletAPIView

from rest_framework.request import Request
from rest_framework.response import Response

from mini_wallet.apps.wallets.models import WalletID
from mini_wallet.core.utils import generate_random_number


class Login(WalletAPIView):

    def post(self, request: Request) -> Response:

        wallet_id = request.data.get('customer_xid')

        wallet = get_object_or_404(WalletID, id=wallet_id)
        random_number = generate_random_number(40)

        token = f"Token {random_number}"
        wallet.token = token
        wallet.save(update_fields=['token'])

        data = {
            "data": {
                "token": wallet.token
            },
            "status": "success"
        }
        return Response(data)
