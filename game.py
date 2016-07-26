from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monster = [
            Goblin(),
            Troll(),
            Dragon()
        ]

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # Check to see if the monster attacks
        # If so, tell the player
        # Check if the player wants to dodge
        # If so, see if the dodge is successful
        # If it is, move on
        # If it's not, remove one player hit point
        # If the monster, isn't attacking, tell that to th player too.

    def player_turn(self):
        # Let the player attack, rest or quit
        # If they attack:
        # See if the attack is successful
        # If so, see if the monster dodges
        # If dodged, print that
        # If not dodged, subtract the right num of hit point from the monster
        # If not a good attack, tell the player
        # If they rest:
        # Call the player.rest() method
        # If they quit, exit the game
        # If they pick anything else, re-run this method

    def cleanup(self):
        # If the monster has no more hit points:
        # up the player's experience
        # print a message
        # Get a new monster

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.momster or self.monsters):
            print(self.player)
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!")
