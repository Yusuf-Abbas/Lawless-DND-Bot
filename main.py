import os
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
bot.load_extension('cogs.Misc')
bot.load_extension('cogs.Events')
bot.load_extension('cogs.Admin')
bot.load_extension('cogs.Music')
bot.load_extension('cogs.Races')
bot.load_extension('cogs.RandomDND')

#You can substitute your token here for your Discord bot
bot.run(os.getenv('TOKEN'))
