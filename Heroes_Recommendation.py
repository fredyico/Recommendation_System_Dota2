from Hero_Database import heroes

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

def get_heroes_by_letter(letter):
    """
    Returns a list of heroes whose names start with the given letter.

    Args:
        letter (str): The first letter to filter heroes by.

    Returns:
        list: A list of hero names starting with the given letter.
    """
    letter = letter.lower()  # Ensure case-insensitivity
    matching_heroes = [hero for hero in heroes.keys() if hero.lower()[4] == letter]
    return matching_heroes

def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nMenu:")
    print("1. Search for heroes based on criteria")
    print("2. Show all heroes by the first letter")
    print("3. Exit")

def main():
    """
    Main function to run the Dota 2 Hero Recommendation System.
    """
    print("Welcome to the Dota 2 Hero Recommendation System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            attributes = ['universal', 'strength', 'agility', 'intelligence']
            complexities = ['low', 'moderate', 'high']
            roles = ['carry', 'support', 'flex']
            tags = ['melee', 'ranged', 'durable', 'disabler', 'nuker', 'initiator', 'escape']

            # Get user inputs
            selected_attribute = get_valid_input(
                "Select an attribute (universal/strength/agility/intelligence): ", 
                attributes
            )
            selected_complexity = get_valid_input(
                "Select complexity (low/moderate/high): ", 
                complexities
            )
            selected_role = get_valid_input(
                "Select a role (carry/support/offlaner/mid/flex/empty): ", 
                roles
            )
            print(f"Available tags: {', '.join(tags)}")
            selected_tags = input("Enter tags separated by commas (e.g., melee,durable): ").strip().lower().split(',')

            # Filter heroes
            matching_heroes = filter_heroes(
                attribute=selected_attribute,
                complexity=selected_complexity,
                role=selected_role,
                tags=selected_tags
            )
            
            if matching_heroes:
                print("\nHeroes matching your criteria:")
                for hero in matching_heroes:
                    print(f"- {hero}")
            else:
                print("\nNo heroes match your criteria. Try different selections.")

        elif choice == '2':
            letter = input("Enter the first letter of the hero name: ").strip()
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single valid letter.")
                continue
            matching_heroes = get_heroes_by_letter(letter)
            if matching_heroes:
                print(f"\nHeroes starting with '{letter.upper()}':")
                for hero in matching_heroes:
                    print(f"- {hero}")
            else:
                print(f"No heroes found starting with '{letter.upper()}'.")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()