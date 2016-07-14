import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    # limit guesses
    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        # safely make an int
        except ValueError:
            print("{} is not a number, asshole!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it right! My number was {}. You lucky bastard!".format(secret_num))
                break
            # too high message
            elif guess > secret_num:
                print("My number is lower than {}.".format(guess))
            # too low message
            else:
                print("My number is higher than {}.".format(guess))
            guesses.append(guess)
    else:
        print("Enough, motherfucker! My number was {}. Fuck off!".format(secret_num))
    # play again
    play_again = raw_input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("You know what B3 is? Bye-Bye-Bitch!")

game()
