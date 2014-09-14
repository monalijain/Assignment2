__author__ = 'sony'

from random import choice
from Paper import *
from Rock import *
from Scissors import *

#Player Class
class Player():
    def play(self): #This method creates a random gesture of computer
        computer=choice(('Rock','Paper','Scissors')) 
        if(computer=='Rock'):
            return Rock()
        if(computer=='Paper'):
            return Paper()
        if(computer=='Scissors'):
            return Scissors()

#HumanPlayer Class
class HumanPlayer(Player): 
    def play(self): #This method asks for the gesture of user/human player
        print("Enter your gesture:rock/paper/scissors")
        sInputFromUser=input().lower()
        if(sInputFromUser=='rock'):
            return Rock()
        if(sInputFromUser=='paper'):
            return Paper()
        if(sInputFromUser=='scissors'):
            return Scissors()
        else:
            print("Wrong gesture. Enter your gesture again")
            return False
