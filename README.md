# ZURI
#Rock Paper Scissors

#import random numbers
import random

#get player choice
while True:
    player_choice = ["r", "p", "s"]
    player_input = input("Select One of R, P or S : R for Rock, P for Paper, S for Scissors").lower().strip()
   
    if player_input == "r" :
        player_input_name = "Rock"
    elif player_input == "p" :
        player_input_name = "Paper"
    else: player_input_name = "Scissors"

    if player_input in player_choice:
        print ("you have selected  " + player_input_name) 
    else :
        print ("Please select a valid option")
        continue

    #computer is playing
    computer_play = random.choice(player_choice)
    if computer_play == "r" :
        computer_play_name = "Rock"
    elif computer_play == "p" :
        computer_play_name = "Paper"
    else: computer_play_name = "Scissors"
    print ( 'Player:' + player_input_name + ' CPU:' + computer_play_name)

    #move interpretation
    if computer_play == player_input:
        print("The game is a draw")
        continue

    elif player_input == 'r' :
        if computer_play == "p" :
            print("You lose, Paper covers Rock ")
        else:
            print("You win, Rock smashes Scissors")

    elif player_input == 'p' :
        if computer_play == "s" :
            print("You lose, Scissors cuts Paper ")
        else:
            print("You win, Paper covers Rock")

    elif player_input == 's' :
        if computer_play == "r" :
            print("You lose, rock smashes scissors ")
        else:
            print("You win, scissors covers paper")
    break     
