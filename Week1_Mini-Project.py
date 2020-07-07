import random
# Rock-paper-scissors-lizard-Spock template

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
def name_to_number(name):        
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        rock = 0
        return rock
    elif name == "Spock":
        Spock = 1
        return Spock
    elif name == "paper":
        paper = 2
        return paper
    elif name == "lizard":
        lizard = 3
        return lizard
    elif name == "scissors":
        scissors = 4
        return scissors
    else:
        print("Error, there is no match to the following input.")
        print(name)

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
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
        print("Error, there is no match to the following input.")
        print(number)

def rpsls(player_choice):    
    # print a blank line to separate consecutive games
    print("")
    # print out the message for the player's choice
    print("Player chooses", player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice) % 5
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer chooses", comp_choice)
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print("Player and computer tie!")
    elif difference == 1 or difference == 2:
        print("Computer wins!")
    elif difference == 3 or difference == 4:
        print("Player wins!")
    else:
        print("Error.", difference)
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


