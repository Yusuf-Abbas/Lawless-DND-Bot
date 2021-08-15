#Work in Progress
import discord
from discord.ext import commands

class Music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def join(self, ctx):
    try:
      voiceChannel = ctx.author.voice.channel
      voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
    except(AttributeError):
      await ctx.send("You're not in a VC, I can't join")
      return
    if voice == None:
      await voiceChannel.connect()
      await ctx.send(f"Joining: **{voiceChannel}**")  
    else: 
      await ctx.send("I'm already in the vc")

  @commands.command()
  async def play(self, ctx, url: str):
    await Music.join(self, ctx)
  
  @play.error
  async def play_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("You need to provide me a URL to the song")


  @commands.command()
  async def die(self, ctx):
    voiceChannel = ctx.author.voice.channel
    voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
    if voice == None:
      await ctx.send("I'm not in a voice call!")
    else:
      await voice.disconnect()
      await ctx.send(f"I left **{voiceChannel}**") 


def setup(client):
    client.add_cog(Music(client))
