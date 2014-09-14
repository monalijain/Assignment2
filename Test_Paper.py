__author__='sony'

#Run this file to test cases in paper class

import unittest
from Paper import *
from Rock import *
from Scissors import *
class PaperTestCase(unittest.TestCase):
    def RunTest(self):
        TestPaper=Paper()
        assert TestPaper.nValue==2,'incorrect paper class'
        assert TestPaper.cmp(Rock())=='True','incorrect cmp function in paper class'
        assert TestPaper.cmp(Paper())=='Same','incorrect cmp function in paper class'
        assert TestPaper.cmp(Scissors())=='False','incorrect cmp function in paper class'
        print("Test of paper class is successfful")
        
TestCase=PaperTestCase()
TestCase.RunTest()
        
      
