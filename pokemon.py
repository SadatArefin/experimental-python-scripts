from collections import Counter
import random

names = ['Seel','Nidorino','Fearow','Vanilluxe','Relicanth','Karrablast','Exeggutor','Diggersby','Mew','Flabébé','Archen','Cryogonal','Cherubi','Barbaracle','Jirachi','Lopunny','Sentret','Heatmor','Bellossom','Drilbur','Gallade','Ivysaur','Sandslash','Aipom','Scatterbug','Carracosta','Frillish','Honedge','Gogoat','Kangaskhan','Hippowdon','Lillipup','Braixen','Wooper','Helioptile','Geodude','Claydol','Furret','Burmy','Clefairy','Sandile','Walrein','Throh','Leavanny','Gengar','Solosis','Eelektross','Foongus','Ferroseed','Sylveon','Marowak','Wailord','Chimchar','Tyrunt','Golem','Mamoswine','Elgyem','Metagross','Panpour','Cinccino','Gloom','Chatot','Onix','Dodrio','Chandelure','Florges','Lilligant','Graveler','Raichu','Sylveon','Minccino','Scolipede','Cresselia','Delphox','Wigglytuff','Seadra','Shellos','Lampent','Infernape','Sawsbuck','Delphox','Delibird','Slaking','Stunfisk','Spritzee','Lillipup','Sharpedo','Gallade','Beheeyem','Charmander','Krookodile','Braixen','Bellsprout','Snorlax','Swinub','Hariyama','Numel','Gardevoir','Mismagius','WormadamTrash Cloak','Dugtrio','Wailmer','Diggersby','Castform','Bisharp','Lileep','Eelektross','Zigzagoon','Tropius','Venomoth','Vibrava','MeowsticFemale','Shieldon','Floatzel','Carnivine','Servine','Swalot','Finneon','Magnezone','Combusken','DarmanitanStandard Mode','Cryogonal','Wynaut','Emboar','Hippopotas','Krabby','Tentacruel','Ludicolo','Bisharp','Claydol','Corsola','Shelmet','Bastiodon','Snorunt','Yanma','Lumineon','Treecko','Zekrom','Azurill','Golduck','Phanpy','WormadamSandy Cloak','Aron','Panpour','Illumise','Zekrom','Shinx','Kabutops','Delibird','Carnivine','Beautifly','Klang','Patrat','Exeggutor','RotomWash Rotom','Dragalge','Kirlia','Dedenne','Electrike','Cherrim','Venomoth','Scolipede','Swirlix','Primeape','Simipour','Skuntank','Glameow','Clamperl','Swablu','Cofagrigus','Hoppip','Torchic','Psyduck','Helioptile','Larvesta','Wigglytuff','Mandibuzz','Empoleon','Shelgon','Spewpa','Charizard','Clamperl','Seedot','Spritzee','Darkrai','Electrike','Virizion','Yanmega','Girafarig','Cranidos','Croagunk','Nidoking','Pupitar','Tympole','Flareon','Lairon','Frogadier','Mime Jr.','Magnemite','Clefable','Gloom','Exeggcute','Bayleef','Staravia','Rattata','Golem','Gible','Kricketune','Seismitoad','Slakoth','Dragonair','Skuntank','Munna','Cacturne','Magmortar','Golbat','Shroomish','Leafeon','Ledian','Cinccino','Armaldo','Froslass','Seadra','Slowbro','Nidorino','KyuremBlack Kyurem','Venomoth','Carnivine','Abomasnow','Zangoose','Honchkrow','Banette','Panpour','Beldum','Ampharos','Wynaut','Medicham','Seviper','Blissey','Azelf',"Farfetch'd",'Relicanth','WormadamPlant Cloak','Sneasel','Fletchling','Larvesta','Cleffa','Mienfoo','Panpour','Arcanine','Hitmonchan','Tangela','Escavalier','Lumineon','Kingdra','Lickilicky','Noctowl','Blissey','Zekrom','Amoonguss','Carracosta','Staravia','Pineco','Swampert','Jirachi','Swanna','Drifblim','Roggenrola','Inkay','Electrike','Cubone','Crobat','Prinplup','Spinarak','Lilligant','Poliwhirl','Vespiquen','Loudred','Grimer','Kadabra','Caterpie','Machop','Slakoth','Foongus','Exeggcute','Gulpin','Delcatty','GroudonPrimal Groudon','Delcatty','Shelmet','Granbull','Shelmet','Bronzong','Tyranitar','Azumarill','Numel','Pyroar','Mantyke','Chikorita','Articuno','Umbreon','Musharna','Jellicent','Spheal','Kadabra','Nosepass','Cobalion','Ducklett','Tirtouga','Accelgor','Fletchling','KyuremWhite Kyurem','Slowbro','Zebstrika','Dugtrio','Stoutland','Shelmet','Dragonair','Hawlucha','RotomFrost Rotom','Gardevoir','Primeape','Swirlix','Gothita','Krabby','Chimchar','Aurorus','Mandibuzz','Nidoqueen','Delibird','Fraxure','Pidove','Altaria','Oddish','Blitzle','Ducklett','Ralts','Baltoy','Jirachi','Avalugg','Clefable','Gurdurr','Seel','Baltoy','Vigoroth','Stunky','Klinklang','Luvdisc','Mew','Sandshrew','Koffing','Pancham','Kirlia','Jirachi','Probopass','Tympole','Spoink','Basculin','Drifblim','Duosion','Primeape','Shelmet','Whirlipede','Roselia','Rufflet','Avalugg','Druddigon','Luxray','Eelektrik','Chespin','Clefable','Graveler','Chatot','Psyduck','Makuhita','Piplup','Pinsir','Lopunny','Tauros','Grimer','Eelektross','Turtwig','Darkrai','Emboar','Cobalion','Talonflame','Nidorino','Dragonair','Larvitar','WormadamSandy Cloak','Wobbuffet','Maractus','Teddiursa','Leavanny','Lampent','Yveltal','Primeape','Plusle','Altaria','Zweilous','Bunnelby','Riolu','Manectric','Lunatone','Wigglytuff','Bouffalant','Leavanny','Cyndaquil','Clamperl','Minccino','Groudon','Scatterbug','Torkoal','Scolipede','Slowking','Rapidash','Ledian','Cofagrigus','Ledian','Mawile','Sealeo','Lickitung','Sharpedo','Kabutops','Beedrill','Spiritomb','Dusclops','Venomoth','Nuzleaf','Gothita','Onix','Aron','Trevenant','Electivire','Blitzle','Feraligatr','Donphan','Skrelp','Ursaring','Hitmontop','Hydreigon','Spritzee','Jumpluff','Arbok','Taillow','Gurdurr','Dustox','Zangoose','Sawsbuck','Volcarona','Simipour','Shedinja','Mienfoo','Wobbuffet','Mantine','Croagunk','Bronzor','Meditite','Elgyem','Hawlucha','Dratini','WormadamTrash Cloak','Moltres','Mr. Mime','Roserade','Dunsparce','Skitty','Skuntank','Joltik','Slowking','Rhyperior','Beautifly','Kyogre','Gallade','Azurill','Aggron','Solrock','Salamence','Weepinbell','Skiploom','Marshtomp','Mienshao','Krookodile','Xerneas','Staraptor','Shiftry','Eelektross','Dewott','Throh','Barbaracle','Ninetales','Sudowoodo','Nosepass','Staryu','Snivy','Hawlucha','Suicune','Weedle','Nincada','Simisage']
primary_types = ['Water','Poison','Normal','Ice','Water','Bug','Grass','Normal','Psychic','Fairy','Rock','Ice','Grass','Rock','Steel','Normal','Normal','Fire','Grass','Ground','Psychic','Grass','Ground','Normal','Bug','Water','Water','Steel','Grass','Normal','Ground','Normal','Fire','Water','Electric','Rock','Ground','Normal','Bug','Fairy','Ground','Ice','Fighting','Bug','Ghost','Psychic','Electric','Grass','Grass','Fairy','Ground','Water','Fire','Rock','Rock','Ice','Psychic','Steel','Water','Normal','Grass','Normal','Rock','Normal','Ghost','Fairy','Grass','Rock','Electric','Fairy','Normal','Bug','Psychic','Fire','Normal','Water','Water','Ghost','Fire','Normal','Fire','Ice','Normal','Ground','Fairy','Normal','Water','Psychic','Psychic','Fire','Ground','Fire','Grass','Normal','Ice','Fighting','Fire','Psychic','Ghost','Bug','Ground','Water','Normal','Normal','Dark','Rock','Electric','Normal','Grass','Bug','Ground','Psychic','Rock','Water','Grass','Grass','Poison','Water','Electric','Fire','Fire','Ice','Psychic','Fire','Ground','Water','Water','Water','Dark','Ground','Water','Bug','Rock','Ice','Bug','Water','Grass','Dragon','Normal','Water','Ground','Bug','Steel','Water','Bug','Dragon','Electric','Rock','Ice','Grass','Bug','Steel','Normal','Grass','Electric','Poison','Psychic','Electric','Electric','Grass','Bug','Bug','Fairy','Fighting','Water','Poison','Normal','Water','Normal','Ghost','Grass','Fire','Water','Electric','Bug','Normal','Dark','Water','Dragon','Bug','Fire','Water','Grass','Fairy','Dark','Electric','Grass','Bug','Normal','Rock','Poison','Poison','Rock','Water','Fire','Steel','Water','Psychic','Electric','Fairy','Grass','Grass','Grass','Normal','Normal','Rock','Dragon','Bug','Water','Normal','Dragon','Poison','Psychic','Grass','Fire','Poison','Grass','Grass','Bug','Normal','Rock','Ice','Water','Water','Poison','Dragon','Bug','Grass','Grass','Normal','Dark','Ghost','Water','Steel','Electric','Psychic','Fighting','Poison','Normal','Psychic','Normal','Water','Bug','Dark','Normal','Bug','Fairy','Fighting','Water','Fire','Fighting','Grass','Bug','Water','Water','Normal','Normal','Normal','Dragon','Grass','Water','Normal','Bug','Water','Steel','Water','Ghost','Rock','Dark','Electric','Ground','Poison','Water','Bug','Grass','Water','Bug','Normal','Poison','Psychic','Bug','Fighting','Normal','Grass','Grass','Poison','Normal','Ground','Normal','Bug','Fairy','Bug','Steel','Rock','Water','Fire','Fire','Water','Grass','Ice','Dark','Psychic','Water','Ice','Psychic','Rock','Steel','Water','Water','Bug','Normal','Dragon','Water','Electric','Ground','Normal','Bug','Dragon','Fighting','Electric','Psychic','Fighting','Fairy','Psychic','Water','Fire','Rock','Dark','Poison','Ice','Dragon','Normal','Dragon','Grass','Electric','Water','Psychic','Ground','Steel','Ice','Fairy','Fighting','Water','Ground','Normal','Poison','Steel','Water','Psychic','Ground','Poison','Fighting','Psychic','Steel','Rock','Water','Psychic','Water','Ghost','Psychic','Fighting','Bug','Bug','Grass','Normal','Ice','Dragon','Electric','Electric','Grass','Fairy','Rock','Normal','Water','Fighting','Water','Bug','Normal','Normal','Poison','Electric','Grass','Dark','Fire','Steel','Fire','Poison','Dragon','Rock','Bug','Psychic','Grass','Normal','Bug','Ghost','Dark','Fighting','Electric','Dragon','Dark','Normal','Fighting','Electric','Rock','Normal','Normal','Bug','Fire','Water','Normal','Ground','Bug','Fire','Bug','Water','Fire','Bug','Ghost','Bug','Steel','Ice','Normal','Water','Rock','Bug','Ghost','Ghost','Bug','Grass','Psychic','Rock','Steel','Ghost','Electric','Electric','Water','Ground','Poison','Normal','Fighting','Dark','Fairy','Grass','Poison','Normal','Fighting','Bug','Normal','Normal','Bug','Water','Bug','Fighting','Psychic','Water','Poison','Steel','Fighting','Psychic','Fighting','Dragon','Bug','Fire','Psychic','Grass','Normal','Normal','Poison','Bug','Water','Ground','Bug','Water','Psychic','Normal','Steel','Rock','Dragon','Grass','Grass','Water','Fighting','Ground','Fairy','Normal','Grass','Electric','Water','Fighting','Rock','Fire','Rock','Rock','Water','Grass','Fighting','Water','Bug','Bug','Grass']
generations = [1,1,1,5,3,5,1,6,1,6,5,5,4,6,3,4,2,5,2,5,4,1,1,2,6,5,5,6,6,1,4,5,6,2,6,1,3,2,4,1,5,3,5,5,1,5,5,5,5,6,1,3,4,6,1,4,5,3,5,5,1,4,1,1,5,6,5,1,1,6,5,5,4,6,1,1,4,5,4,5,6,2,3,5,6,5,3,4,5,1,5,6,1,1,2,3,3,3,4,4,1,3,6,3,5,3,5,3,3,1,3,6,4,4,4,5,3,4,4,3,5,5,3,5,4,1,1,3,5,3,2,5,4,3,2,4,3,5,3,1,2,4,3,5,3,5,4,1,2,4,3,5,5,1,4,6,3,6,3,4,1,5,6,1,5,4,4,3,3,5,2,3,1,6,5,1,5,4,3,6,1,3,3,6,4,3,5,4,2,4,4,1,2,5,1,3,6,4,1,1,1,1,2,4,1,1,4,4,5,3,1,4,5,3,4,1,3,4,2,5,3,4,1,1,1,5,1,4,4,3,4,3,5,3,2,3,3,3,2,4,1,3,4,2,6,5,2,5,5,1,1,1,5,4,2,4,2,2,5,5,5,4,2,3,3,5,4,5,6,3,1,2,4,2,5,1,4,3,1,1,1,1,3,5,1,3,3,3,3,5,2,5,4,2,2,3,6,4,2,1,2,5,5,3,1,3,5,5,5,5,6,5,1,5,1,5,5,1,6,4,3,1,6,5,1,4,6,5,1,2,5,5,3,1,5,5,3,3,3,6,1,5,1,3,3,4,5,3,1,1,1,6,3,3,4,5,3,5,4,5,1,5,5,3,5,6,5,4,5,6,1,1,4,1,3,4,1,4,1,1,5,4,4,5,5,6,1,1,2,4,2,5,2,5,5,6,1,3,3,5,6,4,3,3,1,5,5,2,3,5,3,6,3,5,2,1,2,5,2,3,3,1,3,1,1,4,3,1,3,5,1,3,6,4,5,2,2,6,2,2,5,6,2,1,3,5,3,3,5,5,5,3,5,2,2,4,4,3,5,6,1,4,1,1,4,2,3,4,5,2,4,3,3,4,3,3,3,3,1,2,3,5,5,6,4,3,5,5,5,6,1,2,3,1,5,6,2,1,3,5]

def create_pokemon_dict(key_list, pokemon_names):
    """Create a dictionary grouping Pokemon by a given key (type or generation).
    
    Args:
        key_list: List of keys (types or generations)
        pokemon_names: List of Pokemon names
    
    Returns:
        Dictionary with keys mapping to lists of Pokemon names
    """
    pokemon_dict = {}
    for key, name in zip(key_list, pokemon_names):
        if key not in pokemon_dict:
            pokemon_dict[key] = []
        pokemon_dict[key].append(name)
    return pokemon_dict

def print_pokemon_groups(group_dict, group_label=""):
    """Print Pokemon grouped by their categories with counts.
    
    Args:
        group_dict: Dictionary mapping categories to Pokemon lists
        group_label: Optional prefix for category labels
    
    Returns:
        Total count of unique Pokemon
    """
    total_unique = 0
    for category, pokemon_list in sorted(group_dict.items()):
        unique_pokemon = sorted(set(pokemon_list))
        count = len(unique_pokemon)
        total_unique += count
        category_name = f"{group_label}{category}"
        print(f"{category_name} ({count}): {', '.join(unique_pokemon)}")
    
    print(f"\nTotal unique Pokemon: {total_unique}")
    return total_unique

# Group Pokemon by type
type_groups = create_pokemon_dict(primary_types, names)
print_pokemon_groups(type_groups)

# Group Pokemon by generation
generation_groups = create_pokemon_dict(generations, names)
print_pokemon_groups(generation_groups, "Generation ")

# Generate power levels
random.seed(100)  # For reproducible results
power_levels = [random.randint(50, 150) for _ in names]

# Create sorted list of Pokemon with power levels
pokemon_powers = list(zip(names, power_levels))
sorted_by_power = sorted(pokemon_powers, key=lambda x: x[1], reverse=True)

def display_pokemon_list(pokemon_list, header):
    """Display a list of pokemon with their power levels."""
    print(f"\n{header}")
    for i, (name, power) in enumerate(pokemon_list, 1):
        print(f"{i}. {name} (Power: {power})")

def get_player_choice(max_choice):
    """Get valid player input for pokemon selection."""
    while True:
        try:
            choice = int(input(f"Select your Pokemon (1-{max_choice}, or 0 to autoplay): ")) - 1
            if choice == -1:  # Player chose 0
                return -1  # Special value to indicate autoplay
            if 0 <= choice < max_choice:
                return choice
            print(f"Invalid choice. Please select 1-{max_choice}.")
        except ValueError:
            print(f"Please enter a number between 1 and {max_choice}.")

def handle_battle_round(player_pokemon, computer_pokemon):
    """Handle a single battle round and return points scored."""
    player_name, player_power = player_pokemon
    computer_name, computer_power = computer_pokemon
    
    print(f"\nYou chose {player_name} (Power: {player_power})")
    print(f"Computer chose {computer_name} (Power: {computer_power})")
    
    total_points = player_power + computer_power
    if player_power > computer_power:
        return total_points, 0, "You win this round!"
    elif computer_power > player_power:
        return 0, total_points, "Computer wins this round!"
    elif computer_power == player_power:
        return 0, 0, "It's a tie! No points awarded."

def display_game_result(player_points, computer_points):
    """Display the final game results."""
    print("\nGame Over!")
    if player_points > computer_points:
        winner = "You win!"
    elif computer_points > player_points:
        winner = "Computer wins!"
    elif computer_points == player_points:
        winner = "It's a tie!"
    print(f"{winner} Final score - You: {player_points}, Computer: {computer_points}")

def select_pokemon_teams(rounds):
    """Select random pokemon teams for player and computer."""
    all_pokemon = list(zip(names, power_levels))
    return random.sample(all_pokemon, rounds), random.sample(all_pokemon, rounds)

def process_player_turn(player_pokemon, autoplay):
    """Handle player's turn and return choice."""
    display_pokemon_list(player_pokemon, "Your Pokemon:")
    if autoplay:
        return 0  # Always return 0 when in autoplay mode
    choice = get_player_choice(len(player_pokemon))
    return choice

def get_round_winner(player_points, computer_points):
    """Determine winner based on points."""
    if player_points > computer_points:
        return "You win!"
    elif computer_points > computer_points:
        return "Computer wins!"
    elif computer_points == player_points:
        return "It's a tie!"

def play_round(round_num, player_pokemon, computer_pokemon, autoplay):
    """Play a single round and return points scored."""
    print(f"\nRound {round_num}")
    player_choice = process_player_turn(player_pokemon, autoplay)
    if player_choice == -1:
        player_choice = 0  # Autoplay: always choose the first Pokemon
    computer_choice = random.randint(0, len(computer_pokemon)-1)
    
    return handle_battle_round(
        player_pokemon.pop(player_choice),
        computer_pokemon.pop(computer_choice)
    )

def play_pokemon_game(rounds=5):
    """Main game function."""
    player_pokemon, computer_pokemon = select_pokemon_teams(rounds)
    player_points = computer_points = 0
    autoplay = False
    
    display_pokemon_list(computer_pokemon, "Computer's Pokemon:")
    
    for round_num in range(1, rounds+1):
        round_points_player, round_points_computer, result = play_round(
            round_num, player_pokemon, computer_pokemon, autoplay
        )
        if not autoplay and round_points_player == -1:  # Check if player chose autoplay
            autoplay = True
        player_points += round_points_player
        computer_points += round_points_computer
        print(result)
    
    winner = get_round_winner(player_points, computer_points)
    print(f"{winner} Final score - You: {player_points}, Computer: {computer_points}")


if __name__ == "__main__":
    try:
        rounds = int(input("Enter number of rounds to play: "))
        play_pokemon_game(rounds)
    except ValueError:
        print("Please enter a valid number of rounds.")
        play_pokemon_game()
