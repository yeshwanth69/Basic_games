def random_game():
    import random
    print("Welcome to The Game Random")
    print("please enter your name")
    gamer=input()
    print("So lets play the game",gamer)
    print("i will assume a number between 1 to 50 and u need to guess it", gamer , "but you only have 30 strikes/guesses")
    desirednumber = random.randint(1,50)
    guessed_number = 10
    while(guessed_number<30):
        print("Now Guess a Number")
        guess=input()
        guess=int(guess)
        guessed_number=guessed_number+1
        if type(guess) == "str":
            print("enter a number")
        if(guess>desirednumber):
            print("NO,the desired number is lower than this number")
        if(guess<desirednumber):
            print("NO,the desired number is higher than this number")
        if(guess==desirednumber):
            break;
    if(guess==desirednumber):
        print(gamer,"won the Game")
    result=input("want to play Again y/n")
    if result == "y":
       random_game()
    if result == "n":
       exit()
random_game()
