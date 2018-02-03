'''Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

ch='y'

while(ch!='n' or ch!='N'):
    move_player1=input("enter the move of player 1: ")
    move_player2=input("enter the move of player 2: ")
    if move_player1 == move_player2:
        print("it is a tie")
    else:
        if (move_player1 == "rock" and move_player2 == "scissors") or (move_player1 == "scissors" and move_player2 == "paper") or (move_player1 == "paper" and move_player2 == "rock"):
            print("player 1 won")
        else:
            print("player 2 won")
    ch=(input("if you want to continue enter (y/n)"))
    if ch =='n' or ch=='N':
        break
