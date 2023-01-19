from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def send_verification_otp(email, token):
    try:
        subject = f"SPARE WALLET: Account Verification"
        to = [settings.DEFAULT_FROM_EMAIL]
        from_email = email
        msg_html = render_to_string(
            "common/otp_email.html",
            {"token": token},
        )
        text_content = strip_tags(msg_html)

        mail = EmailMultiAlternatives(subject, text_content, from_email, to)
        mail.attach_alternative(msg_html, "text/html")
        mail.send()
    except Exception as e:
        print(f"account verification email failed:  {e}")