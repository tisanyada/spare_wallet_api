import requests
from datetime import datetime

def send_verification_otp(email, token):
    headers = {
        "authorization": "NzYyNzYxNTc2Nzk2MTI3MjQz.Gu5ZDT.Y59iF4po9pp6zSVJREXydsVIvnNlKBJEew_39Q"
    }
    payload = {
        'content': f""" Spare Wallet Email Verification Code \nRECIPIENT {email} \nVERIFICATION CODE {token} \nTIME OF EVENT {datetime.now().strftime('%A, %d %B, %Y')} {datetime.now().strftime("%H:%M:%S")}
        """
    }
    
    r = requests.post('https://discord.com/api/v9/channels/1062400358690869258/messages', data=payload, headers=headers)
    