from django.utils import timezone
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from mini_wallet.apps.wallets.models import WalletID
from mini_wallet.api.views import WalletAuthenticationView

from mini_wallet.api.response import ErrorResponse

from .forms import DepositForm, WithDrawalsForm


class Wallet(WalletAuthenticationView):

    def get(self, request: Request) -> Response:
        token = request.headers.get('Authorization')

        wallet_id = get_object_or_404(WalletID, token=token)
        if not hasattr(wallet_id, 'wallet'):
            data = {
                "data": "wallet not found",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        response = {
            'status': 'success',
            'data': {
                'wallet': {
                    'id': str(wallet_id.wallet.id),
                    'owned_by': str(wallet_id.wallet.owned_by.id),
                    'status': 'enabled' if wallet_id.wallet.status else "disabled",
                    'enabled_at': timezone.localtime(wallet_id.wallet.enabled_at).strftime('%Y-%m-%d %H:%M:%S') if wallet_id.wallet.enabled_at else "",
                    'balance': wallet_id.wallet.balance
                }
            }
        }
        return Response(response)

    def post(self, request: Request) -> Response:
        token = request.headers.get('Authorization')

        wallet_id = get_object_or_404(WalletID, token=token)
        if not hasattr(wallet_id, 'wallet'):
            data = {
                "data": "wallet not found",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if wallet_id.wallet.status == False:
            wallet_id.wallet.status = True
            wallet_id.wallet.enabled_at = timezone.localtime()
            wallet_id.wallet.save(update_fields=['status', 'enabled_at'])

        response = {
            'status': 'success',
            'data': {
                'wallet': {
                    'id': str(wallet_id.wallet.id),
                    'owned_by': str(wallet_id.wallet.owned_by.id),
                    'status': 'enabled' if wallet_id.wallet.status else "disabled",
                    'enabled_at': timezone.localtime(wallet_id.wallet.enabled_at).strftime('%Y-%m-%d %H:%M:%S') if wallet_id.wallet.enabled_at else "",
                    'balance': wallet_id.wallet.balance
                }
            }
        }
        return Response(response)


class Deposit(WalletAuthenticationView):

    def post(self, request: Request) -> Response:
        token = request.headers.get('Authorization')

        wallet_id = get_object_or_404(WalletID, token=token)
        if not hasattr(wallet_id, 'wallet'):
            data = {
                "data": "wallet not found",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        wallet = wallet_id.wallet
        if not wallet.status:
            data = {
                "data": "wallet inactive",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        form = DepositForm(data=request.data, wallet=wallet)
        if form.is_valid():
            deposit = form.save()
            wallet.balance += deposit.amount
            wallet.save(update_fields=['balance'])

            response = {
                "status": "success",
                "data": {
                    "id": deposit.id,
                    "deposited_by": wallet_id.id,
                    "status": deposit.get_status_display(),
                    "deposited_at": timezone.localtime(deposit.deposited_at).strftime('%Y-%m-%d %H:%M:%S'),
                    "amount": deposit.amount,
                    "reference_id": deposit.reference_id
                }
            }
            return Response(response)

        return ErrorResponse(form=form)


class WithDrawals(WalletAuthenticationView):

    def post(self, request: Request) -> Response:
        token = request.headers.get('Authorization')

        wallet_id = get_object_or_404(WalletID, token=token)
        if not hasattr(wallet_id, 'wallet'):
            data = {
                "data": "wallet not found",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        wallet = wallet_id.wallet
        if not wallet.status:
            data = {
                "data": "wallet inactive",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if wallet.balance == 0.0:
            data = {
                "data": "insufficient balance",
                "status": "failed"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        form = WithDrawalsForm(data=request.data, wallet=wallet)
        if form.is_valid():
            withdrawals = form.save()
            wallet.balance -= withdrawals.amount
            wallet.save(update_fields=['balance'])

            response = {
                "status": "success",
                "data": {
                    "id": withdrawals.id,
                    "deposited_by": wallet_id.id,
                    "status": withdrawals.get_status_display(),
                    "deposited_at": timezone.localtime(withdrawals.withdrawn_at).strftime('%Y-%m-%d %H:%M:%S'),
                    "amount": withdrawals.amount,
                    "reference_id": withdrawals.reference_id
                }
            }
            return Response(response)

        return ErrorResponse(form=form)

