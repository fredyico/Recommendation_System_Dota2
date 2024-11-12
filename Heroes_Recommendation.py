

def greet():
  print("Hi there and welcome to Dota2 Recommendation System!")
  print("We'll help you find the best and suited hero for you.")
  print("What would you like to do?\n 1.Hero based on position/role? \n 2.Counter-Pick suggestion? \n ")

def goodbye():
  print("Thanks for using D2RS. See you next time.")

def choose_hero():
    pass

def hero_position():
    hero_pos = input("Choose the hero position that you would like. 1)Pos1(midlaner)\n 2)Pos2(safelaner/carry)\n 3)Pos3(offlaner)\n 4)Pos4(soft support)\n 5)Pos5(hard support)\n")

def counter_pick_hero():    
    counter_pick = input("What is the hero that you would like to counter?\n")

def Dota2_Recomm_System():
  greet()
  choose_hero()
  goodbye()
