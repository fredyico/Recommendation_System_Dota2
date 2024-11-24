# Dota 2 Hero Recommendation System

A Python-based recommendation system for Dota 2 heroes. This tool allows users to explore heroes based on attributes, roles, complexity, and tags. It also includes a feature to display all heroes starting with a specific letter.

## Features

- Search heroes based on:
  - Attributes: Universal, Strength, Agility, Intelligence
  - Roles: Carry, Support, Flex
  - Complexity: Low, Moderate, High
  - Tags: Melee, Ranged, Durable, Disabler, Nuker, etc.
- Display all heroes starting with a specific letter.
- User-friendly menu with input validation to guide users effectively.

## How it Works

1. Menu Options:
   - Option 1: Search heroes based on criteria.
   - Option 2: Display all heroes whose names start with a specific letter.
   - Option 3: Exit the program.
2. Hero Filtering:
   - Input criteria for attributes, complexity, roles, and tags.
   - Get a list of heroes matching the selected criteria.
3. Hero Search by Letter:
   - Enter a letter to display all heroes starting with that letter.

## Getting Started

### Prerequisites

- Python 3.8 or above installed on your system.

### Installation

1. **Clone the Repository:**

    ```
   git clone https://github.com/fredyico/Recommendation_System_Dota2.git
   cd Recommendation_System_Dota2 
    ```

2. **Run the Program:**

    ```
    python Heroes_Recommendation.py
    ```
## Usage

### Menu Options

Upon running the program, you’ll see the following menu:

```python
Menu:
1. Search for heroes based on criteria
2. Show all heroes by the first letter
3. Exit

```

### Example 1: Search for Heroes Based on Criteria
1. Select Option 1 from the menu.
2. Input your desired criteria:
   - Attribute: strength
   - Complexity: low
   - Role: carry
   - Tags: melee, durable
3. Output:

```python
Heroes matching your criteria:
- Axe

```

### Example 2: Show Heroes by First Letter
1. Select Option 2 from the menu.
2. Input the letter 'a'.
3. Output:

```python
Heroes starting with 'A':
- Anti-Mage
- Axe
- Abaddon

```

### Example 3: Exit the Program
1. Select Option 3 from the menu to exit.

## Hero Database
The hero database is derived from the official Dota 2 website. Heroes are categorized based on:

   - Attributes: Universal, Strength, Agility, Intelligence
   - Roles: Carry, Support, Flex
   - Tags: Melee, Ranged, Durable, Disabler, Nuker, etc.
### Note:
Heroes without explicitly defined roles on the Dota 2 website are categorized as 'flex'.

## Development Progress
* Hero database creation
* Menu implementation
* Input validation
* Filtering functionality
* Display heroes by first letter
* Code refactoring and cleanup
* Autocomplete feature for hero names
* Additional hero details (abilities, synergies, counters)

## Contributing
Contributions are welcome! If you'd like to add features or improve the project, follow these steps:

1. Fork the repository:

```bash
git fork https://github.com/fredyico/Recommendation_System_Dota2.git
```
2. Create a branch for your feature:

```bash
git checkout -b feature-name
```
3. Commit your changes:

```bash
git commit -m "Added feature-name"
```
4. Push your changes to your forked repository:

```bash
git push origin feature-name
```
5. Submit a pull request.