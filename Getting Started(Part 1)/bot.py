import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load your token from .env
load_dotenv()
token = os.getenv('TOKEN')

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True # Enable bot to receive message content

# Create the bot instance with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents) 
# You can change the command prefix to whatever you want

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Run the bot
bot.run(token)
