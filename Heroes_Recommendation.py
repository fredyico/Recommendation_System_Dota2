from Hero_Database import caracteristics, heroes, heroes_string, heroes_atribute, heroes_role, heroes_complexity, heroes_tags, key_caracteristics

def greet():
  print("Hi there and welcome to Dota2 Recommendation System!")
  print("We'll help you find the best and suited hero for you.")

def goodbye():
  print("Thanks for using D2RS. See you next time.")

def hero_by_letter():
  pass

def hero_by_traits():
  pass

def hero_by_multiple_traits():
  pass

#def hero_sinergy():
#  pass

#def counter_hero():
#  pass

def show_heroes():
  see_heroes = input("Would you like to see the list of heroes again? Enter y/n: ")
  if see_heroes == "y":
    print(heroes_string)

def show_caracteristics():
  see_caracteristics = input("Would you like to see the list of heroes caracteristics? Enter y/n: ")
  if see_caracteristics == "y":
    print(f"{key_caracteristics[0]}: {heroes_atribute}")
    print(f"{key_caracteristics[1]}: {heroes_role}")
    print(f"{key_caracteristics[2]}: {heroes_complexity}")
    print(f"{key_caracteristics[3]}: {heroes_tags}")

def Dota2_Recomm_System():
  greet()
  user_choice = int(input("What would you like to do?\n 1.Recommendation heroes by first letter?\n 2.Recommendation heroes by characteristics?\n 3.Recommendation heroes by multiple characteristics?\n"))
  if user_choice == 1:
    hero_by_letter()
  elif user_choice == 2:
    hero_by_traits()
  elif user_choice == 3:
    hero_by_multiple_traits()    
  goodbye()

#show_heroes()
#show_caracteristics()