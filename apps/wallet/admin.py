from django.contrib import admin
from .models import Wallet, DebitCard


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pkid",
        "wallet_number",
        "wallet_balance",
        "wallet_user",
    ]


@admin.register(DebitCard)
class DebitCardAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pkid",
        "card_name",
        "card_number",
        "card_type",
        "card_expiration",
        "card_user",
    ]
