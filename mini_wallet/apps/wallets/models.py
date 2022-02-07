import uuid
from django.db import models
from django.utils import timezone


class WalletID(models.Model):
    """
    Wallet ID
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class Wallet(models.Model):
    """
    Wallet
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owned_by = models.ForeignKey(WalletID, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    enabled_at = models.DateTimeField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.owned_by


class Deposit(models.Model):
    """
    Deposit
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    class STATUS(models.IntegerChoices):
        SUCCESS = 1, 'success'
        FAILED = 2, 'failed'

    status = models.IntegerField(choices=STATUS.choices, default=STATUS.SUCCESS)
    deposited_at = models.DateTimeField(default=timezone.localtime)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference_id = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self):
        return self.wallet.id


class Withdrawal(models.Model):
    """
    Withdrawal
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    class STATUS(models.IntegerChoices):
        SUCCESS = 1, 'success'
        FAILED = 2, 'failed'

    status = models.IntegerField(choices=STATUS.choices, default=STATUS.SUCCESS)
    withdrawn_at = models.DateTimeField(default=timezone.localtime)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference_id = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self):
        return self.wallet.id