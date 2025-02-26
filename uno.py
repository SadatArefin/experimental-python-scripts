# All possible colors in uno
import random


colors = ['red', 'yellow', 'green', 'blue', 'wild']

# All possible values in uno
unique_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'skip', 'reverse', 'draw_two', 'wild', 'wild_draw_four', 'draw_four']

# All possible actions in uno
actions = ['skip', 'reverse', 'draw_two', 'wild', 'wild_draw_four', 'draw_four']

players = ['player1', 'player2', 'player3', 'player4']

# All possible directions in uno
directions = ['clockwise', 'counter-clockwise']

# shuffle the deck and deal 7 cards to each player
deck = [(color, value) for color in colors for value in unique_values]
random.shuffle(deck)
player_hands = {player: [] for player in players}
for _ in range(7):
    for player in players:
        player_hands[player].append(deck.pop())

# initialize the discard pile
discard_pile = [deck.pop()]

# initialize the game state
current_player = players[0]

# initialize the game direction
current_direction = directions[0]

# initialize the game state
game_over = False

# initialize the winner
winner = None

# initialize the number of cards to draw
cards_to_draw = 0

# start the game
while not game_over:
    # get the top card of the discard pile
    top_card = discard_pile[-1]

    # get the current player's hand
    hand = player_hands[current_player]

    # check if the current player has any valid moves
    valid_moves = []
    for card in hand:
        if card[0] == top_card[0] or card[1] == top_card[1] or card[0] == 'wild':
            valid_moves.append(card)

    # if the current player has no valid moves, draw cards until a valid move is found
    if not valid_moves:
        while not valid_moves:
            if not deck:  # if deck is empty
                if len(discard_pile) > 1:  # ensure there's more than just the top card
                    top_card = discard_pile.pop()
                    deck.extend(discard_pile[:-1])  # add all cards except the last one
                    random.shuffle(deck)
                    discard_pile = [top_card]
                else:
                    break  # no more cards available to draw
            
            if cards_to_draw > 0:
                for _ in range(cards_to_draw):
                    if deck:
                        player_hands[current_player].append(deck.pop())
                cards_to_draw = 0
            elif deck:  # only draw if there are cards available
                player_hands[current_player].append(deck.pop())
                
            for card in player_hands[current_player]:
                if card[0] == top_card[0] or card[1] == top_card[1] or card[0] == 'wild':
                    valid_moves.append(card)
                    break

    # if the current player has a valid move, play the move
    if valid_moves:
        # play a random valid move
        move = random.choice(valid_moves)
        player_hands[current_player].remove(move)
        discard_pile.append(move)

        # check if the player has uno
        if len(player_hands[current_player]) == 1:
            print(f'{current_player} has uno!')

        # check if the player has won
        if not player_hands[current_player]:
            game_over = True
            winner = current_player

        # handle special actions
        if move[1] == 'skip':
            pass
        elif move[1] == 'reverse':
            current_direction = directions[(directions.index(current_direction) + 1) % 2]
        elif move[1] == 'draw_two':
            cards_to_draw += 2
        elif move[1] == 'wild':
            pass
        elif move[1] == 'wild_draw_four':
            cards_to_draw += 4
        elif move[1] == 'draw_four':
            cards_to_draw += 4

    # switch to the next player
    if current_direction == 'clockwise':
        current_player = players[(players.index(current_player) + 1) % len(players)]
    else:
        current_player = players[(players.index(current_player) - 1) % len(players)]

# print the winner
print(f'{winner} wins!')