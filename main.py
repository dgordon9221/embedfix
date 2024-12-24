import os
import re
from urllib.parse import urlsplit, urlunsplit

import discord
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    url = re.search(r'(?P<url>https?://[^\s]+)', message.content)
    if not url:
        return
    parsedUrl = urlsplit(url.group('url'))

    match parsedUrl.netloc:
        case 'x.com' | 'www.x.com' | 'twitter.com' | 'www.twitter.com':
            await message.reply(urlunsplit(parsedUrl._replace(netloc='fxtwitter.com',query='')))
        case 'instagram.com' | 'www.instagram.com':
            fullUrl = urlunsplit(parsedUrl._replace(netloc='ddinstagram.com'))
            response = requests.get(fullUrl)
            if response.status_code != 404:
                await message.reply(fullUrl)
        case _:
            return

client.run(os.environ['DISCORD_BOT_TOKEN'])

