import random

def start_game():
    # Declare the necesary variables for the program
    correct_number = random.randint(1, 10)
    tries = 0
    highscore = 0

    print("""
    -----------------------------------------
    Welcome to the Number Guessing Game!
    -----------------------------------------
    """)
    # Start the loop of the game
    while True:
        tries += 1
        try:
            guess = int(input("Pick a number between 1 and 10:\n"))
        except ValueError:
            print("Please input a number between 1 and 10.")
            continue
        if guess > 10 or guess < 1:
            print("Please choose a number between 1 and 10.")
        elif guess < correct_number:
            print("It is higher!")
        elif guess > correct_number:
            print("It is lower!")
        else:
            print("You got it it took you {} times.".format(tries))
            if highscore == 0 or tries < highscore:
                highscore = tries
            # End of the game
            while True:
                play_again = input("Whould you like to play again? [y]es/[n]o: ")
                if play_again == "n":
                    print("Closing game, see you next time!")
                    quit()
                elif play_again == "y":
                    tries = 0
                    correct_number = random.randint(1, 10)
                    print("The HIGHSCORE is {}".format(highscore))
                    break
                else:
                    print("Please choose an option.")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()