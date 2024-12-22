# import the random library
import random

######################################################
############# define the roll function ################
######################################################
def roll(): # 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value) # we have to come up with random number from one to six

    return roll
# example to test the random function
# value = roll()
# print(value)

######################################################################################
######################### setting up the number of players ###########################
######################################################################################
while True: # using a while loop to keep asking a player to give a valid input, until a valid input is given we dont break out of the loop
    players = input("Enter the number of players (2 - 4): ") # setting the number of players
    if players.isdigit(): # setting up a condition to determine if the input provided is a valid whole number using the isdigit function
        players = int(players) # as player input is always taken as  string we use this to convert the string input into a number or an integer
        if 2 <= players <= 4: # setting up a condition to check if the number provided is between 2 and 4 as required to break out of the while loop, because we have valid number of players
            break
        else: 
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

#########################################################
################ simulating player turns ################
#########################################################

max_score = 50 # max score a player can get 
player_scores = [0 for _ in range(players)] # storing all player scores in a list(array), this list is going to change size based on the number of players we have. using list comprehension
print(player_scores)

while max(player_scores) < max_score: # while the maximum is less than the max score we keep looping
    for player_idx in range(players): # taking care of player turns and if a player wants to keep rolling 
        print("\n player number", player_idx + 1, "turn has just started!") # to alert a player that its now their turn
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True: # if player wants to keep rolling
            should_roll = input("Would you like to roll (y)? ") # asking for using input and if the want to roll 
            if should_roll.lower() != "y": # using .lower() to check for both upper case and lower case inputs i.e if input is not equal to "y" which is yes we break out of the code
                break
            value = roll() # if input is equal to "y" we call the roll function and roll
            if value == 1: # when a player rolls a 1 the turn is done
                print("You rolled 1! Turn done!")
                current_score = 0 # current score get reset to zero when a player rolls a 1
                break
            else: 
                current_score += value # if a player didnt roll a 1 we add the value to the current score of the player i.e if player rolled a 6 after current score is already 5 == 5 + 6
                print("You rolled a:", value) # tell the player what they rolled 
            
            print("Your score is:", current_score) # current score of the player i.e summing up their rolls 

        player_scores[player_idx] += current_score # total score of a player after they finish thier turn
        print("Your total score is:", player_scores[player_idx])


max_score = max(player_scores) # finding the winner using the max function on our list of players_scores to determine winner
winning_idx = player_scores.index(max_score) # using the index function to determine where the maximum score is which tells us which player it is
print("Players number", winning_idx + 1, "is the winner with a score of: ", max_score) # plus 1 to take care of the indexing in a list which starts from 0, because we have player 1 - 4
