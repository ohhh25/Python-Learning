# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)
    global remaining_guesses
    remaining_guesses = 7
    print("New game. Range is 0 to 100")
    print("Number of remaining guesses is", remaining_guesses)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print("")
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print("")
    secret_number = random.randrange(0, 1000)
    global remaining_guesses
    remaining_guesses = 10
    print("New game. Range is 0 to 1000")
    print("Number of remaining guesses is", remaining_guesses)
    
    
def input_guess(guess):
    # main game logic goes here
    print("")
    #storing and print the input, guess
    guess = int(guess)
    print("Guess was", guess)
    #updating the number of remaining_guesses
    global remaining_guesses
    remaining_guesses = remaining_guesses - 1
    print("Number of remaining guesses is", remaining_guesses)
    #creating variables for outcomes
    out_of_guesses = remaining_guesses == 0
    correct = guess == secret_number
    higher = guess < secret_number
    lower = guess > secret_number
    #creating outcomes
    if out_of_guesses:
        print("You ran out of guesses. The number was", secret_number)
        print("")
        new_game()
    elif correct:
        print("Correct!")
    elif higher:
        print("Higher!")
    elif lower:
        print("Lower!")
    else:
        print("Error.", guess, secret_number)
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
frame.stop()
frame.start()

# always remember to check your completed program against the grading rubric
