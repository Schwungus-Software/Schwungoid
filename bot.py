import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = "+", intents = intents)

#region Commands
@bot.command(name = "coin")
async def coin(ctx):
    await ctx.send(random.choice(["Heads!", "Tails!"]))
#endregion

bot.run(TOKEN)
