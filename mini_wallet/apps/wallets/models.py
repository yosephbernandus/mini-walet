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
    owned_by = models.OneToOneField(WalletID, related_name="wallet", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    enabled_at = models.DateTimeField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.owned_by.id}"


class Deposit(models.Model):
    """
    Deposit
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="deposits")
    class STATUS(models.IntegerChoices):
        success = 1, 'success'
        failed = 2, 'failed'

    status = models.IntegerField(choices=STATUS.choices, default=STATUS.success)
    deposited_at = models.DateTimeField(default=timezone.localtime)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference_id = models.UUIDField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.id}"


class Withdrawal(models.Model):
    """
    Withdrawal
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="withdrawals")
    class STATUS(models.IntegerChoices):
        success = 1, 'success'
        failed = 2, 'failed'

    status = models.IntegerField(choices=STATUS.choices, default=STATUS.success)
    withdrawn_at = models.DateTimeField(default=timezone.localtime)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference_id = models.UUIDField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.id}"
