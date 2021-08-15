class human:
  def __init__(self):
    pass
  
  txt = None

  with open("./Categories/Humanoid/Human.txt") as text:
    txt = text.readlines()
  text.close()

  def out(self):
    print(self.txt)