import random
import json
from discord.ext import commands

abilityScoreList = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]

dndBackgrounds = {}
with open('./DataDND/dndBackgrounds.json', 'r') as text:
  dndBackgrounds = json.load(text)
text.close()

dndRaces = {}
with open('./DataDND/dndRaces.json', 'r') as text2:
  dndRaces = json.load(text2)
text2.close()


dndClasses = {}
with open('./DataDND/dndClasses.json','r') as file:
  dndClasses = json.load(file)
file.close()


def getOneScore():
    theList = [0, 0, 0, 0]
    for i in range(4):
      theList[i] = random.randint(1,6)
    theList.remove(min(theList))
    return(sum(theList))

def getSixScores():
  scores = [0,0,0,0,0,0]
  for x in range(6):
    scores[x] = getOneScore()
  return scores
def getPoints():
  totalPoint, buffs, debuffs = 4, 0, 0
  for x in range(0,2):
    if random.randint(0,2) == 0:
      totalPoint += 0
    elif random.randint(0,2) == 1:
      buffs += 1
      totalPoint -= 1
    else:
      debuffs += 1
      totalPoint +=1
    return(totalPoint, buffs, debuffs)

def getMods(points):
  oneMods, twoMods, threeMods = 0, 0, 0
  while points > 0:
    if(points >= 3):
        var = random.randint(1, 3)
        points = points - var
        if var == 3:
            threeMods +=1
        elif var == 2:
            twoMods += 1
        else:
            oneMods += 1
    elif(points >=2):
        var = random.randint(1,2)
        points = points - var
        if var == 2:
            twoMods +=1
        else:
            oneMods += 1
    else:
        var = 1
        points = points -1
        oneMods +=1
  return(oneMods, twoMods, threeMods)

def getClass():
  return random.choice(list(dndClasses))

def getSubClass(playerClass):
  return(random.choice(list(dndClasses.get(playerClass).get("Subclasses"))))

def getRace():
  return random.choice(list(dndRaces))

def getSubRace(playerRace):
  return (random.choice(dndRaces.get(playerRace)))

def getBackground():
  return random.choice(list(dndBackgrounds.get("Backgrounds")))

def getSkills(playerClass):
  if playerClass == "Barbarian":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Bard":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),3))
  elif playerClass == "Cleric":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Druid":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Fighter":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Monk":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Paladin":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Ranger":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),3))
  elif playerClass == "Rogue":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),4))
  elif playerClass == "Sorcerer":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Warlock":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Wizard":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  elif playerClass == "Artificer":
    return(random.sample(list(dndClasses.get(playerClass).get("Skill Proficiencies")),2))
  else:
    return "What did you do...."

class RandomDND(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def rc(self,ctx):
    playerRace = getRace()
    playerSubRace = getSubRace(playerRace)
    playerBackground = getBackground()
    
    playerClass = getClass()
    playerSubClass = getSubClass(playerClass)
    playerSkills = getSkills(playerClass)
    
    playerScores = getSixScores()
    playerScoreTotal = sum(playerScores)
    
    await ctx.send(f'Generating random DND character:\nStrength: {playerScores[0]}\nDexterity: {playerScores[1]}\nConstitution: {playerScores[2]}\nIntelligence: {playerScores[3]}\nWisdom: {playerScores[4]}\nCharisma: {playerScores[5]}\n\nScore total: {playerScoreTotal}\n\nYour race is: {playerRace}\nYour subrace is: {playerSubRace}\nYour background is: {playerBackground}\nYour class: {playerClass}\nYour subclass: {playerSubClass}\nYour skills: {playerSkills}')

  @commands.command()
  async def rco(self, ctx):
    #Will be done when One Piece Races are finished
    await ctx.send("In Progress")


  
  @commands.command()
  async def rcm(self, ctx):
    #Will be done when MegaMan data is made
    await ctx.send("In Progress")
    #points = 0(totalPoints), 1(buffs), 2(debuffs)
    #modules = 0(Level one), 1(Level 2), 2(Level 3)
    points = getPoints()
    modules = getMods(points[0])
    playerClass = getClass()
    playerSkills = getSkills(playerClass)
    twoRandomAbility = random.sample(abilityScoreList, 2)
    threeRandomAbility = random.sample(abilityScoreList, 3)
    
def setup(client):
    client.add_cog(RandomDND(client))