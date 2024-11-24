
# Talin koskosky
# CTI110
# 11-22-24
# making a basic game where you create characters and fight each other. 
# P5hW








import random

# Function to create a character
def create_character():
    """
    Prompts the user to input attributes for a character and returns a dictionary.
    """
    name = input("Enter the character's name: ")
    health = int(input("Enter the character's health (integer): "))
    attack_points = int(input("Enter the character's attack points (integer): "))
    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points
    }
    print(f"Character '{name}' created successfully! 🎉")
    return character

# Function to display all characters
def display_characters(character_list):
    """
    Displays the attributes of all characters in the provided list of dictionaries.
    """
    if not character_list:
        print("No characters available to display.")
    else:
        print("\nCharacters:")
        for index, char in enumerate(character_list, start=1):
            print(f"Character {index}:")
            for key, value in char.items():
                print(f"  {key.capitalize()}: {value}")
        print()

# Function to simulate a battle
def character_battle(attacker, defender):
    """
    Simulates an attack between two characters.
    Reduces the defender's health based on the attacker's attack points.
    Returns the updated defender dictionary.
    """
    damage = random.randint(1, attacker['attack_points'])
    defender['health'] -= damage
    print(f"\n⚔️ {attacker['name']} attacks {defender['name']} and deals {damage} damage!")
    if defender['health'] <= 0:
        defender['health'] = 0
        print(f"💀 {defender['name']} has been defeated!")
    else:
        print(f"🩸 {defender['name']} now has {defender['health']} health remaining.")
    return defender

# Main function to control the game
def main():
    """
    Main function to manage the game flow.
    """
    characters = []
    while True:
        print("\nMenu:")
        print("1. Create a character")
        print("2. Display all characters")
        print("3. Character battle")
        print("4. Exit the game")
        choice = input("Enter your choice: ")

        if choice == "1":
            character = create_character()
            characters.append(character)
        elif choice == "2":
            display_characters(characters)
        elif choice == "3":
            if len(characters) < 2:
                print("Not enough characters for a battle! Create more characters first.")
            else:
                display_characters(characters)
                attacker_index = int(input("Choose the attacker (enter the number): ")) - 1
                defender_index = int(input("Choose the defender (enter the number): ")) - 1
                if attacker_index == defender_index:
                    print("A character cannot attack itself!")
                else:
                    attacker = characters[attacker_index]
                    defender = characters[defender_index]
                    defender = character_battle(attacker, defender)
                    #Update the defender in the list
                    characters[defender_index] = defender
        elif choice == "4":
            print("Exiting the game. Thanks for playing! 🎮")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
