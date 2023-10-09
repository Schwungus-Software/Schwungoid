import random

import discord

from discord.ext import commands

class Fun(commands.Cog):
    """Fun"""

    @commands.command(brief = "Heads or Tails?")
    async def coin(self, ctx):
        """Coin Flip"""

        await ctx.send(random.choice(["Heads!", "Tails!"]))

class Admin(commands.Cog):
    """Admin"""

    async def cog_check(self, ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        else:
            await ctx.send("No admin perms, no coochie")
            return False

    @commands.command(brief = "Deletes a specified amount of messages")
    async def purge(self, ctx, amount: int):
        """Purge"""

        messages = await ctx.channel.purge(limit = amount + 1)
        await ctx.send("Cleared {} messages".format(len(messages)))
