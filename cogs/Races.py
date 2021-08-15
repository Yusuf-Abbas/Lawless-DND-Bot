#NEEDS WORK

import discord
from discord.ext import commands


class Races(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group()
  async def raceinfo(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send("Invalid race.")

  @raceinfo.command(name='gnome')
  async def _gnome(self, ctx):
    with open("./Categories/Humanoid/Gnome.txt") as text:
      await ctx.send(text.readlines()[0].replace("\\n", '\n')
    )
    text.close()
  
  @raceinfo.command(name='dwarf')
  async def _dwarf(self, ctx, subrace=None):
    if subrace is None:
      with open("./Categories/Humanoid/Dwarf.txt") as text:
        await ctx.send(text.readlines()[0].replace("\\n", '\n'))
      text.close()
      await ctx.send(
        ">>> **Subraces.** Hill dwarf (``$raceinfo dwarf hill``), Mountain dwarf (``$raceinfo dwarf mountain``)"
      )
    elif subrace == 'hill':
      with open("./Categories/Humanoid/Subraces/HillDwarf.txt") as text:
        await ctx.send(text.readlines()[0].replace("\\n", '\n'))
      text.close()
    elif subrace == 'mountain':
      with open("./Categories/Humanoid/Subraces/MountainDwarf.txt") as text:
        await ctx.send(text.readlines()[0].replace("\\n", '\n'))
      text.close()
    else:
      await ctx.send("Invalid dwarf subrace.")
  
  @raceinfo.command(name='halfling')
  async def _halfling(self, ctx):
    with open("./Categories/Humanoid/Halfling.txt") as text:
      await ctx.send(text.readlines()[0].replace("\\n", '\n'))
    text.close()

  @raceinfo.command(name='human')
  async def _human(self, ctx):
    with open("./Categories/Humanoid/Human.txt") as text:
      await ctx.send(text.readlines()[0].replace("\\n", '\n'))
    text.close()


def setup(client):
	client.add_cog(Races(client))
