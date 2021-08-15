import discord
import random
from discord.ext import commands

#reading in the data
leaveMessages = {}
with open("./Data/leaveMessages.txt") as text2:
  leaveMessages = text2.readlines()
text2.close()
joinMessages = {}
with open ("./Data/joinMessages.txt") as text:
  joinMessages = text.readlines()
text.close()

class Events(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('I AM VERIFIED BOT')
    #await self.client.get_channel(817100498880167936).send('*italics*')
    await self.client.change_presence(activity = discord.Game("DND"))

  @commands.Cog.listener()
  async def on_member_join(self, member):
    await self.client.get_channel(357344671850037249).send(random.choice(joinMessages).replace("123", (f'{member}'[:-5])))

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    await self.client.get_channel(357344671850037249).send(f'Good riddance {member}. I always accomplish my mission.')


def setup(client):
  client.add_cog(Events(client))
