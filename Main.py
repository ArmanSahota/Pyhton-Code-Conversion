# Main.py
from Player import Player
from Menu import Menu

def main():22
players = [
        Player("Player1", 1),
        Player("Player2", 2),
        Player("Player3", 3),
        Player("Player4", 4),
        Player("Player5", 5)
    ]

while True:
        Menu.print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            Menu.display_all_players(players)
        elif choice == '2':
            Menu.display_players_with_odd_numbers(players)
        elif choice == '3':
            letter = input("Enter a letter: ")
            Menu.display_players_with_letter(players, letter)
        elif choice == '4':
            Menu.add_player(players)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
