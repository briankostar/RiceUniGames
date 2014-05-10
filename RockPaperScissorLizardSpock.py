# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print number, "is not an accepted number!"
    
def name_to_number(name):
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name =="Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print name, "is not an accepted name!"

def rpsls(name): 

    # convert name to player_number using name_to_number
    print "Player chooses", name
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    print "Computer chooses", number_to_name(comp_number)
    # compute difference of player_number and comp_number modulo five
    num_diff = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if num_diff == 0:
        print "Player and Computer ties!"
    elif num_diff <= 2:
        print "Player wins!"
    elif num_diff > 2:
        print "Computer wins!"
    else: 
        print "ain't nobody winnin today nigga"
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    # print results
    print
    
    
# testing code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


