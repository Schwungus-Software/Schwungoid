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

help_command = commands.DefaultHelpCommand(no_category = "General")

bot = commands.Bot(
    command_prefix = ["+", "¤", "No "],
    intents = intents,
    help_command = help_command
)

#region Commands

class Fun(commands.Cog):
    """Fun"""
    
    @commands.command(brief = "Heads or Tails?")
    async def coin(self, ctx):
        """Coin Flip"""
        
        await ctx.send(random.choice(["Heads!", "Tails!"]))

class Admin(commands.Cog):
    """Admin"""
    
    @commands.command(brief = "Deletes a specified amount of messages")
    async def purge(self, ctx, amount: int):
        """Purge"""
        
        if ctx.author.guild_permissions.administrator:
            messages = await ctx.channel.purge(limit = amount + 1)
            
            await ctx.send("Cleared {} messages".format(len(messages)))

#endregion

@bot.event
async def on_ready():
    await bot.add_cog(Fun())
    await bot.add_cog(Admin())

bot.run(TOKEN)
