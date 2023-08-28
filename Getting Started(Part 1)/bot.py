import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import tensorflow as tf
import numpy as np

# Load your token from .env
load_dotenv()
token = os.getenv('TOKEN')

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True # Enable bot to receive message content

# Create the bot instance with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents) 
# You can change the command prefix to whatever you want

loaded_model = tf.keras.models.load_model('saved_model')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')



# COMMANDS
@bot.command()
async def hello(ctx):
    await ctx.send("Hello World!")

@bot.command()
async def predict(ctx):
    try:
        input_value = float(ctx.message.content.split()[1])
        prediction = loaded_model.predict(np.array([[input_value]]))[0][0]
        
        await ctx.send(f"Prediction for {input_value}: {prediction:.2f}")
    except:
        await ctx.send("Invalid Input! Please use !predict [number]")

# Run the bot
bot.run(token)
