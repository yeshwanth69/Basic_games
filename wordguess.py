import string
import random
def game_man():
    # welcoming the user
    name = input("What is your name? ")
    print("Hello, " + name, "It is time to play hangman!")
    print("Start guessing.....!")
    # here we set the secret
    word =''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    # creates a variable with an empty value
    guesses = ''
    # determine the number of turns
    turns = 30
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1

        if failed == 0:
            print("You won the game! " + name)
            break
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1

            print("your guess is not exact!")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("Game over " + name)
    check=input("want to play Again y/n")
    if check == "y":    
     game_man()
    if check == "n":
        exit()
game_man()                
