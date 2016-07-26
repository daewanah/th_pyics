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
        if self.monster.attack():
        # If so, tell the player
            print("{} is attacking!".format(self.monster))
        # Check if the player wants to dodge
            if raw_input("Dodge? Y/n: ").lower() == 'y':
        # If so, see if the dodge is successful
                if self.player.dodge():
        # If it is, move on
                    print("You dodged the attack!")
        # If it's not, remove one player hit point
                else:
                    print("You got hit anyway!")
                    self.player.hit_points -= 1
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
        # If the monster, isn't attacking, tell that to th player too.
        else:
            print("{} isn't attacking this turn.".format(self.monster))

    def player_turn(self):
        # Let the player attack, rest or quit
        player_choice = raw_input("[A]ttack, [R]est, [Q]uit: ").lower()
        # If they attack:
        if player_choice == 'a':
        # See if the attack is successful
            print("You're attacking {}!".format(self.monster))
        # If so, see if the monster dodges
            if self.player.attack():
        # If dodged, print that
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))
        # If not dodged, subtract the right num of hit point from the monster
                else:
                    if self.player.level_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}!".format(self.monster, self.weapon))
        # If not a good attack, tell the player
            else:
                print("You missed!")
        # If they rest:
        elif player_choice == 'r':
        # Call the player.rest() method
            self.player.rest()
        # If they quit, exit the game
        elif player_choice == 'q':
            sys.exit()
        # If they pick anything else, re-run this method
        else:
            self.player_turn()

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
