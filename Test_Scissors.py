__author__='sony'

#Run this file to test case on scissors class
import unittest
from Paper import *
from Rock import *
from Scissors import *
class ScissorsTestCase(unittest.TestCase):
    def RunTest(self):
        TestScissors=Scissors()
        assert TestScissors.nValue==3,'incorrect scissors class'
        assert TestScissors.cmp(Scissors())=='Same','incorrect cmp function in scissors class'
        assert TestScissors.cmp(Paper())=='True','incorrect cmp function in scissors class'
        assert TestScissors.cmp(Rock())=='False','incorrect cmp function in scissors class'
        print("Test of scissors class is successful")
        
TestCase=ScissorsTestCase()
TestCase.RunTest()
        
