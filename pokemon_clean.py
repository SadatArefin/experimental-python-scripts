from typing import List, Tuple, Dict
import random
from dataclasses import dataclass

@dataclass
class Pokemon:
    name: str
    type: str
    health: int
    attack: int
    defense: int

class PokemonGame:
    def __init__(self):
        self.pokemon_data = [
            Pokemon("Pikachu", "Electric", 35, 55, 40),
            Pokemon("Charizard", "Fire", 78, 84, 78),
            Pokemon("Blastoise", "Water", 79, 83, 100),
            Pokemon("Venusaur", "Grass", 80, 82, 83),
            Pokemon("Mewtwo", "Psychic", 106, 110, 90),
        ]
        self.player_points = 0
        self.computer_points = 0

    def get_pokemon_choice(self) -> Pokemon:
        print("\nAvailable Pokemon:")
        for i, pokemon in enumerate(self.pokemon_data, 1):
            print(f"{i}. {pokemon.name}")
        
        while True:
            try:
                choice = int(input("\nChoose your Pokemon (1-5): ")) - 1
                if 0 <= choice < len(self.pokemon_data):
                    return self.pokemon_data[choice]
                print("Please choose a number between 1 and 5")
            except ValueError:
                print("Please enter a valid number")

    def battle_round(self, player_pokemon: Pokemon, computer_pokemon: Pokemon) -> Tuple[int, int, str]:
        print(f"\nYou chose {player_pokemon.name}")
        print(f"Computer chose {computer_pokemon.name}")

        player_power = (player_pokemon.attack + player_pokemon.defense) * random.uniform(0.8, 1.2)
        computer_power = (computer_pokemon.attack + computer_pokemon.defense) * random.uniform(0.8, 1.2)

        if player_power > computer_power:
            return 1, 0, "You won this round!"
        elif computer_power > player_power:
            return 0, 1, "Computer won this round!"
        return 0, 0, "It's a tie!"

    def display_game_result(self) -> None:
        print("\n=== Game Over ===")
        print(f"Final Score - You: {self.player_points}, Computer: {self.computer_points}")
        
        if self.player_points > self.computer_points:
            print("Congratulations! You won the game!")
        elif self.computer_points > self.player_points:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

    def play(self, rounds: int = 3) -> None:
        print("\nWelcome to Pokemon Battle!")
        
        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}")
            player_pokemon = self.get_pokemon_choice()
            computer_pokemon = random.choice(self.pokemon_data)
            
            round_points_player, round_points_computer, result = self.battle_round(
                player_pokemon, computer_pokemon
            )
            
            self.player_points += round_points_player
            self.computer_points += round_points_computer
            
            print(f"{result}")
            print(f"Score - You: {self.player_points}, Computer: {self.computer_points}")
        
        self.display_game_result()

def main():
    game = PokemonGame()
    try:
        rounds = int(input("Enter number of rounds to play (default 3): ") or 3)
        game.play(rounds)
    except ValueError:
        print("Invalid input. Using default 3 rounds.")
        game.play()

if __name__ == "__main__":
    main()