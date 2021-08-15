class gnome:
  def __init__(self):
    print("HI")
  
  txt = None
  
  with open("./Categories/Humanoid/Gnome.txt") as text:
    txt = text.readlines()
  text.close()
  
  def out(self):
    print(self.txt)