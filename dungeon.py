import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_location():
    # monster = random
    # door = random
    # start = random

    # if monster, door, start are the same, do it again

    # return monster, door, start

def move_player(player, move):
    # Get the player's current location
    # If move is LEFT, y - 1
    # If move is RIGHT, y + 1
    # If move is UP, x - 1
    # If move is DOWN, x + 1
    return player

def get_move(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # If player's y is 0, remove LEFT
    # If player's x is 0, remove UP
    # If player's y is 2, remove RIGHT
    # If player's x is 2, remove DOWN
    return MOVES

    while True:
        print("Welcome to the dungeon!")
        print("You're currently in the room {}.") # fill with the player position
        print("You can move {}.") # fill in with available moves
        print("Enter 'QUIT' to quit.")

        move = raw_input("> ")
        move = move.upper()

        if move == 'QUIT':
            break

        # If it's a good move, change the player's position
        # If it's a bad move, don't change anything
        # If the new player position is the door, they win!
        # If the new player position is the monster, they lose!
        # Otherwise, continue.
