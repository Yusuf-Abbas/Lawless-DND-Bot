import discord
from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_role('Post Yusuf God Powers')
  async def kick(self, ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)

  @kick.error
  async def kick_error(self,ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
      await ctx.send("Not even here, dude.")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("You need to select someone to kick")
    elif isinstance(error, discord.ext.commands.errors.MissingRole):
      await ctx.send("You don't have that power")
    elif isinstance(error, discord.ext.commands.errors.CommandInvokeError):
      await ctx.send("That is forbidden")
    else:
      await ctx.send("I dunno what you did, but I can't fix **THAT** error")


  @commands.command()
  async def messageperson(self, ctx, member: discord.Member, *, message):
    try:
      await member.send(message)
    except(discord.Forbidden):
      await ctx.send("User blocked me :/")
      return

  @messageperson.error
  async def messageperson_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
      await ctx.send("They're not in the server")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("You need to select someone to message")
  
  @commands.command()
  async def turnoff(self, ctx):
    await ctx.send("Powering off")
    await self.client.close()


def setup(client):
    client.add_cog(Admin(client))