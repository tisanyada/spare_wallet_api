import requests
from datetime import datetime

def send_verification_otp(email, token):
    try:
        headers = {
            "authorization": "NzYyNzYxNTc2Nzk2MTI3MjQz.GMKIc9.zZA0N87BXUcD7ppFMlbh8lTPIGEM7SexLnxVKk"
        }
        payload = {
            'content': f"""Spare Wallet Email Verification Code \nRECIPIENT {email} \nVERIFICATION CODE {token} \nTIME OF EVENT {datetime.now().strftime('%A, %d %B, %Y')} {datetime.now().strftime("%H:%M:%S")}
            """
        }
        
        r = requests.post('https://discord.com/api/v9/channels/1062400358690869258/messages', data=payload, headers=headers)
        res = r.json()
        # print(res)
        print(f"[SEND OTP SUCCESS] :: {res['id']}")
    except Exception as e:
        print(f"[SEND OTP ERROR] :: {e}")