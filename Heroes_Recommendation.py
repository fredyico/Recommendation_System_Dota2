from Hero_Database import caracteristics, heroes


heroes_string = ""
for hero in heroes.keys():
  heroes_string += f"{hero[0:]}\n"

heroes_atribute = ""
heroes_role = ""
heroes_complexity = ""
heroes_tags = ""

for a_r_c_t, values in caracteristics.items():
  if a_r_c_t == 'attributes':
    heroes_atribute += f"{values}, "
  elif a_r_c_t == 'role':
    heroes_role += f"{values}, "
  elif a_r_c_t == 'complexity':
    heroes_complexity += f"{values}, "
  elif a_r_c_t == 'tags':
    heroes_tags += f"{values}, "

#print(heroes_string)

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

def show_heroes():
  see_heroes = input("Would you like to see the list of heroes again? Enter y/n: ")
  if see_heroes == "y":
    print(heroes_string)

def show_caracteristics():
  see_caracteristics = input("Would you like to see the list of heroes caracteristics? Enter y/n: ")
  if see_caracteristics == "y":
    print(f"{caracteristics.keys()[0]}: {heroes_atribute}, ")
    print(f"{caracteristics.keys()[1]}: {heroes_role}, ")
    print(f"{caracteristics.keys()[2]}: {heroes_complexity}, ")
    print(f"{caracteristics.keys()[3]}: {heroes_tags}, ")

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


show_caracteristics()