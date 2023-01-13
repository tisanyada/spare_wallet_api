from django.db import models

from apps.user.models import User
from apps.common.models import TimeStampedUUIDModel
from apps.common.id_generator import wallet_card_id_generator


class Wallet(TimeStampedUUIDModel):
    wallet_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    wallet_balance = models.CharField(max_length=255, blank=True, null=True)
    wallet_user = models.ForeignKey(User, related_name="wallet_user", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.wallet_number} - {self.wallet_balance}"


class DebitCard(TimeStampedUUIDModel):
    card_name = models.CharField(max_length=255, blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    card_expiration = models.DateField(blank=True, null=True)
    card_user = models.ForeignKey(User, related_name="card_user", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_name} - {self.card_balance}"
