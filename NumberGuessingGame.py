# "Guess the number" 
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# initialize global variables
secret_number = 0
remaining_guess = 7
game_mode = 100

# helper function to start and restart the game
def new_game(low, high):
    global secret_number
    global remaining_guess
    secret_number = random.randrange(low, high)
    print "New Game. Range is", low, "to", high
    print "Number of Remaining Guesses", remaining_guess, "\n"
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global remaining_guess
    global game_mode
    remaining_guess = 7
    game_mode = 100
    new_game(0, 100)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global remaining_guess
    global game_mode
    remaining_guess = 10
    game_mode = 1000
    new_game(0, 1000)
    
def input_guess(guess):
    global remaining_guess
    remaining_guess -= 1
    guessed_number = int(guess)
    if guessed_number > secret_number:
        print "Guess was:", guessed_number
        print "Remaining Guesses:", remaining_guess
        print "Go lower!\n"
    elif guessed_number < secret_number:
        print "Guess was:", guessed_number
        print "Remaining Guesses:", remaining_guess 
        print "Go higher!\n"
    else: 
        print "You win!"
        
    if remaining_guess == 0 or guessed_number == secret_number:
        print "Game Fished! Answer was:", secret_number, "\n"
        if game_mode == 100:
            range100()
        else:
            range1000()

    
# create frame
f = simplegui.create_frame("Guess the number!", 300, 200)


# register event handlers for control elements
f.add_label("Press below to start New Game:")
f.add_button("Range: [0, 100)", range100, 200)
f.add_button("Range: [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game(0, 100)
f.start()

