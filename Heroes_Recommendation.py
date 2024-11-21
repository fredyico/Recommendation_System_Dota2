from Hero_Database import caracteristics, heroes, heroes_string

def greet():
  print("Welcome to the Dota 2 Hero Recommendation System!")
  print("We'll help you find the best and suited hero for you.")

def goodbye():
  print("Thanks for using D2RS. See you next time.")

def get_valid_input(prompt, options):
    """
    Prompt the user for input and validate it against a list of valid options.
    Args:
        prompt (str): The message to display to the user.
        options (list): A list of valid input options.
    Returns:
        str: The validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        else:
            print(f"Invalid input. Please choose from: {', '.join(options)}")

def select_criterias():
  attributes = ['universal', 'strength', 'agility', 'intelligence']
  complexities = ['low', 'moderate', 'high']
  roles = ['carry', 'support', 'empty']

  print("Welcome to the Dota 2 Hero Recommendation System!")
    
    # Prompt user for attribute selection
  selected_attribute = get_valid_input(
      "Select an attribute (universal/strength/agility/intelligence): ", 
        attributes)
  print(f"You selected attribute: {selected_attribute.capitalize()}")

    # Prompt user for complexity selection
  selected_complexity = get_valid_input(
        "Select complexity (low/moderate/high): ", 
        complexities)
  print(f"You selected complexity: {selected_complexity.capitalize()}")

    # Prompt user for role selection
  selected_role = get_valid_input(
        "Select a role (carry/support/offlaner/mid/empty): ", 
        roles)
  print(f"You selected role: {selected_role.capitalize()}")

    # Continue with the recommendation logic using the selected criteria
  print("\nFetching heroes that match your criteria...\n")

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
  see_heroes = input("Would you like to see the list of heroes? Enter y/n: ")
  if see_heroes.lower() == "y":
    print(heroes_string)

def show_caracteristics():
  see_caracteristics = input("Would you like to see the list of heroes caracteristics? Enter y/n: ")
  if see_caracteristics.lower() == "y":
    print(f"{key_caracteristics[0]}: {heroes_atribute}")
    print(f"{key_caracteristics[1]}: {heroes_role}")
    print(f"{key_caracteristics[2]}: {heroes_complexity}")
    print(f"{key_caracteristics[3]}: {heroes_tags}")

def Dota2_Recomm_System():
  greet()
  show_heroes()

  show_caracteristics()
    
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