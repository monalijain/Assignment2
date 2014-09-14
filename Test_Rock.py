__author__='sony'

#Run this file to test cases in rock class

import unittest
from Paper import *
from Rock import *
from Scissors import *
class RockTestCase(unittest.TestCase):
    def RunTest(self):
        TestRock=Rock()
        assert TestRock.nValue==1,'incorrect rock class'
        assert TestRock.cmp(Rock())=='Same','incorrect cmp function in rock class'
        assert TestRock.cmp(Paper())=='False','incorrect cmp function in rock class'
        assert TestRock.cmp(Scissors())=='True','incorrect cmp function in rock class'
        print("Test of rock class is successfful")
        
TestCase=RockTestCase()
TestCase.RunTest()
        
