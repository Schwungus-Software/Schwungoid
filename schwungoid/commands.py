import random
import discord
import asyncio

from discord.ext import commands

class Refuse(commands.CommandError):
    """Raise this if you just want to flip the user off."""

    def __init__(self, reason):
        self.reason = reason

class Fun(commands.Cog):
    """Fun"""

    @commands.command(brief = "Heads or Tails?")
    async def coin(self, ctx):
        """Coin Flip"""

        await ctx.send(random.choice(["Heads!", "Tails!"]))

class Admin(commands.Cog):
    """Admin"""

    async def cog_check(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            raise Refuse(":no_entry_sign: Cannot use admin commands")

        return True

    @commands.command(brief = "Deletes a specified amount of messages")
    async def purge(self, ctx, amount: int):
        """Purge"""
        
        await ctx.message.delete()
        
        messages = await ctx.channel.purge(limit = amount)
        
        await ctx.send("Cleared {} messages".format(len(messages)), delete_after = 5.0)
