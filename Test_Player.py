__author__='sony'

#Run this file to test cases on Player and Human Player Class
from Paper import *
from Rock import *
from Scissors import *
from Player import *

import unittest
class PlayerTestCase(unittest.TestCase):
    def RunTest(self):
        TestPlayer=Player()
        GestureTestPlayer=TestPlayer.play()
        assert GestureTestPlayer.nValue==1 or GestureTestPlayer.nValue==2 or GestureTestPlayer.nValue==3, 'incorrect class player'
        print("Test on player class is successful\n")

TestCase=PlayerTestCase()
TestCase.RunTest()

class HumanPlayerTestCase(unittest.TestCase):
    def RunTest(self):
        TestHumanPlayer=HumanPlayer()
        print("Enter the input as 'Rock' in the input prompt")
        GestureTestHumanPlayer=TestHumanPlayer.play()
        #Enter the input as rock
        assert GestureTestHumanPlayer.nValue==1,'incorrect human player class'
        print("Test on Human Player is successful")

TestCase=HumanPlayerTestCase()
TestCase.RunTest()
