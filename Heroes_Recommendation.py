from Hero_Database import heroes

def greet():
  print("*** Welcome to the Dota 2 Hero Recommendation System! ***")
  print("**We'll help you find the best and suited hero for you.**\n")

def goodbye():
  print("\n*** Thanks for using D2RS. See you next time.***")

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

def filter_hero_by_letter():
  heroes_found = []
  letters = list(map(chr, range(ord('a'), ord('z')+1)))
  letter_heroes = get_valid_input("Select a letter to list heroes starting with that letter: ", letters)
  for hero_name in heroes.keys():
    if hero_name[4].lower() == letter_heroes:
      heroes_found.append(hero_name)
      
  print(f"\nHeroes matching letter '{letter_heroes}' criteria:")
  for hero in heroes_found:
    print(f"- {hero}")

def searching_hero_from_criterias():
# Define valid options
  attributes = ['universal', 'strength', 'agility', 'intelligence']
  complexities = ['low', 'moderate', 'high']
  roles = ['carry', 'support', 'flex']
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
      "Select a role (carry/support/flex): ", 
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
      
def choose_search_method():
  options = ['a','b']
  selected_search_method = get_valid_input("Select the method to list your heroes:\na) Search by the first name letter \nb) Search by specific criterias(attributes,complexity,roles,tags)", options)
  if selected_search_method == 'a':
    filter_hero_by_letter()
  elif selected_search_method == 'b':
    searching_hero_from_criterias()
    

def main():
  try_again = ""
  greet()
  while try_again != "n":
    choose_search_method()
    try_again = input("would you like to search again? y/n ")
    if try_again == "n":
      goodbye()
      
        
  

if __name__ == "__main__":
    main()