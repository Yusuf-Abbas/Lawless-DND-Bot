import discord
import random
from discord.ext import commands

ooc = {}
with open("./Data/quotes.txt") as oocfile:
  ooc = oocfile.readlines()
oocfile.close()

class Misc(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def quote(self, ctx):
    await self.client.get_channel(827432757596520469).send(random.choice(ooc).replace('##', '\n'))
    #await ctx.send(random.choice(ooc).replace('##', '\n'))
  
  @commands.command()
  async def cointoss(self, ctx, amount: int):
    heads = 0
    tails = 0
    for x in range(0, amount):
      flip = random.randint(0, 1)
      if(flip == 0):
        heads += 1 
      else:
        tails += 1
    await ctx.send(f'Heads: {heads}\nTails: {tails}')
  
  @cointoss.error
  async def cointoss_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("You didn't say how many! I'll flip one in case")
      await Misc.cointoss(self, ctx, 1)
  
  @commands.command()
  async def roll(self, ctx, numberOfDice: int, numberOfSides: int):
    total = 0
    rolls = {}
    for x in range(0, numberOfDice):
      rolls[x] = random.randint(1, numberOfSides)
      await ctx.send(f'Die {x+1}: {rolls[x]}')
      total += rolls[x]
    await ctx.send(f'Total: {total}')

  @roll.error
  async def rollerror(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("Whoa there, sport! You didn't use the command correctly. Let's try again, okay?\nHere's an example: Enter \"$roll 1 6\" to roll one six-sided die.")

  @commands.command()
  async def kaung(self, ctx):
    await ctx.send('What do you call a detective crocodile? \nAn investigator')
    await ctx.send("I also hate Kaung btw")
  

def setup(client):
    client.add_cog(Misc(client))






