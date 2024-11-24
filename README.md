    Dota 2 Hero Recommendation System
A Python-based recommendation system for Dota 2 heroes. This tool allows users to explore heroes based on attributes, roles, complexity, and tags. Additionally, it includes a feature to display all heroes starting with a specific letter.

    Features
* Search heroes based on:
    * Attributes (Universal, Strength, Agility, Intelligence)
    * Roles (Carry, Support, Flex)
    * Complexity (Low, Moderate, High)
    * Tags (e.g., Melee, Ranged, Durable, Disabler, Nuker, etc.)
* Display all heroes starting with a specific letter.
* User-friendly menu with input validation.
    How It Works
1. Menu Options:

* Option 1: Search heroes based on criteria.
* Option 2: Display all heroes whose names start with a specific letter.
* Option 3: Exit the program.

2. Hero Filtering:

* Input criteria for attributes, complexity, roles, and tags.
* Get a list of heroes matching the selected criteria.

3. Hero Search by Letter:

* Enter a letter to display all heroes starting with that letter.

    Getting Started
Prerequisites
* Python 3.8 or above installed on your machine.
    Clone the Repository

git clone https://github.com/fredyico/Recommendation_System_Dota2.git
cd Recommendation_System_Dota2
    Run the Program
python Heroes_Recommendation.py
    Usage
Example 1: Search for Heroes Based on Criteria
Select Option 1 from the menu.
Input your desired criteria:
Attribute: strength
Complexity: low
Role: carry
Tags: melee, durable
Output:
diff
Copiar código
Heroes matching your criteria:
- Axe
Example 2: Show Heroes by First Letter
Select Option 2 from the menu.
Input the letter a.
Output:
diff
Copiar código
Heroes starting with 'A':
- Anti-Mage
- Axe
- Abaddon
Example 3: Exit the Program
Select Option 3 from the menu to exit.
Hero Database
The hero database is derived from the official Dota 2 website. Heroes are categorized based on:

Attributes: Universal, Strength, Agility, Intelligence.
Roles: Carry, Support, Flex.
Tags: Includes descriptors like Melee, Ranged, Durable, Disabler, etc.
Note:
Heroes without explicitly defined roles on the Dota 2 website are categorized as flex.

Development Progress
 Hero database creation
 Menu implementation
 Input validation
 Filtering functionality
 Display heroes by first letter
 Code refactoring and cleanup
 Autocomplete feature for hero names
 Additional hero details (abilities, synergies, counters)
Contributing
Contributions are welcome! If you'd like to add features or improve the project, feel free to fork the repository and submit a pull request.

Steps to Contribute:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m "Added new feature").
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Dota 2 hero data is based on official information from the Dota 2 website.
Built as part of a portfolio project to practice Python and data structures.