import random

# make a list of words
words = [
    'apple',
    'orange',
    'banana',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

while True:
    start = input("Press enter/return to start, or enter 'q' to quit.")
    if start.lower() == 'q':
        break
    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(set(secret_word)):
        # draw guessed letter, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print(' ')
        print('Strike: {}/7'.format(len(bad_guesses)))
        print(' ')
        # take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(set(secret_word)):
                print("You win! The word was {}.".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You did not guess it! My secret word was {}.".format(secret_word))
