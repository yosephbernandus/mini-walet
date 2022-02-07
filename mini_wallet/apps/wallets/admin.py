from django.contrib import admin
from .models import WalletID, Wallet, Withdrawal, Deposit


admin.site.register(WalletID)
admin.site.register(Wallet)
admin.site.register(Withdrawal)
admin.site.register(Deposit)
