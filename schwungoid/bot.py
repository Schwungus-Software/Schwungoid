import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Expected to get a Discord bot token through the DISCORD_TOKEN environment variable")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

help_command = commands.DefaultHelpCommand(no_category = "General")

bot = commands.Bot(
    command_prefix = ["+", "¤", "No ", "№ "],
    intents = intents,
    help_command = help_command
)

@bot.event
async def on_ready():
    from .commands import Fun, Admin
    await bot.add_cog(Fun())
    await bot.add_cog(Admin())

bot.run(TOKEN)
