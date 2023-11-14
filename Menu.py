# Menu
from Player import Player
class Menu:
    @staticmethod
    def display_all_players(players):
        print("All Players:")
        for player in players:
            print(player)

    @staticmethod
    def display_players_with_odd_numbers(players):
        print("Players with Odd Numbers:")
        for player in players:
            if player.number % 2 != 0:
                print(player)

    @staticmethod
    def display_players_with_letter(players, letter):
        print(f"Players with Names Starting with '{letter}':")
        for player in players:
            if player.name.lower().startswith(letter.lower()):
                print(player)

    @staticmethod
    def add_player(players):
        name = input("Enter the player's name: ")
        number = int(input("Enter the player's number: "))
        new_player = Player(name, number)
        players.append(new_player)
        print(f"{new_player.name} has been added to the list.")

    @staticmethod
    def print_menu():
        print("\nMenu:")
        print("1. Display all players")
        print("2. Display players with odd numbers")
        print("3. Display players with names that start with a letter")
        print("4. Add a player")
        print("5. Exit")