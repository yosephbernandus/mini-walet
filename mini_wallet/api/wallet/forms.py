from mini_wallet.apps.wallets.models import Wallet, Withdrawal, Deposit
from django import forms

from typing import Dict, Any


class DepositForm(forms.Form):
    amount = forms.DecimalField()
    reference_id = forms.CharField()

    def __init__(self, wallet: Wallet, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.wallet = wallet

    def clean(self) -> Dict:
        if self.errors:
            return self.cleaned_data

        reference_id = self.cleaned_data['reference_id']
        if Deposit.objects.filter(reference_id=reference_id).exists():
            raise forms.ValidationError("reference_id already exists", "reference_id_exists")

        return self.cleaned_data

    def save(self) -> Deposit:
        deposit = self.wallet.deposits.create(
            status=Deposit.STATUS.success,
            amount=self.cleaned_data['amount'],
            reference_id=self.cleaned_data['reference_id']
        )

        return deposit


class WithDrawalsForm(forms.Form):
    amount = forms.DecimalField()
    reference_id = forms.CharField()

    def __init__(self, wallet: Wallet, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.wallet = wallet

    def clean(self) -> Dict:
        if self.errors:
            return self.cleaned_data

        reference_id = self.cleaned_data['reference_id']
        if Withdrawal.objects.filter(reference_id=reference_id).exists():
            raise forms.ValidationError("reference_id already exists", "reference_id_exists")

        return self.cleaned_data

    def save(self) -> Withdrawal:
        withdrawals = self.wallet.withdrawals.create(
            status=Withdrawal.STATUS.success,
            amount=self.cleaned_data['amount'],
            reference_id=self.cleaned_data['reference_id']
        )

        return withdrawals
