import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.user.models import User
from .models import Wallet, DebitCard
from apps.common.otp import send_verification_otp
from apps.common.id_generator import wallet_card_id_generator


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        try:
            wallet = Wallet.objects.get(wallet_user=instance)

            print(f"[SIGNALS] User wallet|debit_card already exists")
        except Wallet.DoesNotExist:
            user = User.objects.get(pkid=instance.pkid)
            
            WALLET_ID = wallet_card_id_generator()
            DEBITCARD_ID = wallet_card_id_generator()

            date_now = datetime.date.today()
            years_to_add = date_now.year + 4

            expiration_date = date_now.replace(year=years_to_add).strftime("%Y-%m-%d")

            Wallet.objects.create(
                wallet_number=WALLET_ID,
                wallet_balance="0.00",
                wallet_user=instance,
            )
            DebitCard.objects.create(
                card_name=f"{instance.last_name} {instance.first_name}",
                card_number=DEBITCARD_ID,
                card_type="VISA",
                card_expiration=expiration_date,
                card_user=instance,
            )
            
            print(f'[OTP] :: {user.account_activation_otp}')
            send_verification_otp(instance.email, user.account_activation_otp)
            print(f"[SIGNALS] Successfully created wallet|debit_card for user with mail address :: {instance.email}")
