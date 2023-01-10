import discord
from discord.ext import commands
import openai

openai.api_key = "openaikeykeykeykey"
client = discord.Client()

# Add bot to server
@client.event
async def on_ready():
    print('Bot is ready!')


@client.event
async def on_message(message):
    # Check that the message isn't from the bot itself
    if message.author == client.user:
        return
    else:
        response = openai.Completion.create(engine="text-davinci-003", prompt=message.content, max_tokens=200)
        await message.channel.send(response['choices'][0]['text'])

client.run('discordkeykeykeykey')
