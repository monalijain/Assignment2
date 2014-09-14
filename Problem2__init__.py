__author__ = 'sony'

#Main file for Rock Paper Scissor Game
#Run this file

from Paper import *
from Rock import *
from Scissors import *
from Player import *

ScoreCard=[0]*2 #Initializing score card fpr two players
bWantToPlay=True #Variable: Does the human player wants to play or not
print("Let's play rock paper scissors")

while(bWantToPlay):
    Player1=Player() #Creating Player 1 using Player Class
    GesturePlayer1=Player1.play() #Asking for gesture of computer player
    Player2=HumanPlayer() #Creating Player 2 using HumanPlayer Class
    
    #Asking User for gesture rock/paper/scissor
    GesturePlayer2=Player2.play() 
    if(GesturePlayer2==False): 
        GesturePlayer2=Player2.play()
        
    #Comparing the gestures of both players
    Compare=GesturePlayer2.cmp(GesturePlayer1)
    if(Compare=='Same'): #if both gestures are same, the match is draw
        ScoreCard[0]=ScoreCard[0]+1
        ScoreCard[1]=ScoreCard[1]+1
        print("This game is draw")
        print("Computer's gesture is",GesturePlayer1.printf())
        print("Your gesture is",GesturePlayer2.printf())
        print("ScoreCard: Computer's Score:",ScoreCard[0],", Your Score:",ScoreCard[1])
    else:
        if(Compare=='True'): #if user's gesture is better,he wins
            ScoreCard[1]=ScoreCard[1]+1
            print("You win this game")
            print("Computer's gesture is",GesturePlayer1.printf())
            print("Your gesture is",GesturePlayer2.printf())
            print("ScoreCard: Computer's Score:",ScoreCard[0],", Your Score:",ScoreCard[1])
        else: #else, he loses
            ScoreCard[0]=ScoreCard[0]+1
            print("You lost this game")
            print("Computer's gesture is",GesturePlayer1.printf())
            print("Your gesture is",GesturePlayer2.printf())
            print("ScoreCard: Computer's Score:",ScoreCard[0],", Your Score:",ScoreCard[1])
    #Asking user if he wants to play again 
    print("Do you want to play again (Yes/No)")
    sUserInput=input().lower()
    if(sUserInput=='no'):
        break
