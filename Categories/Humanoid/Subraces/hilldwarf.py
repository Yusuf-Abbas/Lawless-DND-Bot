class hilldwarf:
  def __init__(self):
    pass
  
  txt = None

  with open("./Categories/Humanoid/Subraces/HillDwarf.txt") as text:
    txt = text.readlines()
  text.close()

  def out(self):
    print(self.txt)