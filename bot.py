import os
import discord
import requests
import json
import asyncio
import dotenv

dotenv.load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            # await message.channel.send('Hello! i am a bot! ') 
            embed = discord.Embed(
                title="Hello!", 
                description="I am a bot! I can send you memes and jokes!",
                color=discord.Color.blue()
            )
            await message.channel.send(embed=embed)


        if message.content.startswith('$meme'):
            meme_url = get_meme()
            embed = discord.Embed(
                title="Meme",
                description="Here is a meme for you!",
                color=discord.Color.blue()
            )
            embed.set_image(url=meme_url)
            await message.channel.send(embed=embed)


        if message.content.startswith('$joke'):
            joke = get_joke()
            embed = discord.Embed(
                title="Joke",
                description=joke,
                color=discord.Color.blue()
            )
            await message.channel.send(embed=embed)

        if message.content.startswith('$purge'):
            if message.author.guild_permissions.manage_messages:
                await message.channel.purge(limit=int(message.content.split()[1]))
            else:
                await message.channel.send('You do not have permission to use this command.')  

        if message.content.startswith('$help'):
            embed = discord.Embed(
                title="🤖 Bot Commands",
                description="Here are the commands you can use:",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="$meme", 
                value="Get a meme", 
                inline=False
            )
            embed.add_field(
                name="$joke", 
                value="Get a joke", 
                inline=False
            )
            embed.add_field(
                name="$help", 
                value="Show this help message", 
                inline=False
            )
            embed.add_field(
                name="$hello", 
                value="Say hello to the bot", 
                inline=False
            )
            embed.add_field(
                name="$purge [number]", 
                value="Delete specified number of messages (Requires Manage Messages permission)", 
                inline=False
            )
            await message.channel.send(embed=embed)


def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(response.text)
    return json_data['setup'] + ' ' + json_data['punchline']



intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)

