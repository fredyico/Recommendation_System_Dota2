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

def filter_heroes(attribute=None, complexity=None, role=None, tags=None):
    """
    Filter heroes based on selected criteria.

    Args:
        attribute (str): The selected attribute.
        complexity (str): The selected complexity.
        role (str): The selected role.
        tags (list): A list of selected tags.

    Returns:
        list: A list of heroes matching the criteria.
    """
    filtered = []
    for hero, data in heroes.items():
        if attribute and data['attributes'] != attribute:
            continue
        if complexity and data['complexity'] != complexity:
            continue
        if role and role not in data['role']:
            continue
        if tags and not all(tag in data['tags'] for tag in tags):
            continue
        filtered.append(hero)
    return filtered

def main():
    print("Welcome to the Dota 2 Hero Recommendation System!")
    
    # Define valid options
    attributes = ['universal', 'strength', 'agility', 'intelligence']
    complexities = ['low', 'moderate', 'high']
    roles = ['carry', 'support', 'offlaner', 'mid', 'empty']
    tags = ['melee', 'ranged', 'durable', 'disabler', 'nuker', 'initiator', 'escape']

    # Get user input for each criterion
    selected_attribute = get_valid_input(
        "Select an attribute (universal/strength/agility/intelligence): ", 
        attributes
    )
    selected_complexity = get_valid_input(
        "Select complexity (low/moderate/high): ", 
        complexities
    )
    selected_role = get_valid_input(
        "Select a role (carry/support/offlaner/mid/empty): ", 
        roles
    )
    print(f"Available tags: {', '.join(tags)}")
    selected_tags = input("Enter tags separated by commas (e.g., melee,durable): ").strip().lower().split(',')

    # Filter heroes based on user inputs
    matching_heroes = filter_heroes(
        attribute=selected_attribute,
        complexity=selected_complexity,
        role=selected_role,
        tags=selected_tags
    )
    
    # Display the results
    if matching_heroes:
        print("\nHeroes matching your criteria:")
        for hero in matching_heroes:
            print(f"- {hero}")
    else:
        print("\nNo heroes match your criteria. Try different selections.")

if __name__ == "__main__":
    main()




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

def Dota2_Recomm_System():
  greet()
  show_heroes()
    
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