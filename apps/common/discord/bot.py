import discord
import responses
from datetime import datetime


# async def send_email_verification(message, user_message, is_private):
async def send_email_verification(message, email, token, is_private):
    try:
        date_time = datetime.now()
        # response = responses.get_response(user_message)
        embed = discord.Embed(
            title="Spare Wallet Email Verification Code",
            description="",
        )
        embed.add_field(
            name="RECIPIENT",
            value=email,
            inline=True
        )
        embed.add_field(
            name="VERIFICATION CODE",
            value=token,
            inline=True
        )
        embed.add_field(
            name="TIME",
            value=f"{date_time.strftime('%A, %d %B, %Y')}",
            inline=True
        )
        
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
    except Exception as e:
        print(f'{e} :: an error occured')
        
        
def run_discord_bot():
    TOKEN = 'MTA2MjQwNDg1MDQyOTczOTA1MQ.GjYsiN.Aj_OHauv2BzPu3R5HaFh6Z6bybavaJcDicQAOM'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    channel = client.get_channel(1062399726714109972)
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await channel.send('Hello')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said "{user_message}" ({channel})')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_email_verification(message, user_message, is_private=True)
        else:
            await send_email_verification(message, user_message, is_private=False)
            
    client.run(TOKEN)