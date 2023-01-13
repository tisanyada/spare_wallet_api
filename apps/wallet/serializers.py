from rest_framework import serializers

from .models import Wallet, DebitCard


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "pkid",
            "wallet_number",
            "wallet_balance",
            "wallet_user",
        ]
class DebitCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCard
        fields = [
            "id",
            "pkid",
            "card_name",
            "card_number",
            "card_type",
            "card_expiration",
            "card_user",
        ]
