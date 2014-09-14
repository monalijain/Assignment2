__author__ = 'sony'

#Paper class to create Paper object

class Paper():
    nValue=2 #assigning value 2 to paper

    def cmp(self, other): #cmp method to compare diferent gestures
        nDiff=other.nValue-self.nValue
        if(nDiff%3==1):
            return 'False'
        if(nDiff==0):
            return 'Same'
        if(nDiff%3==2):
            return 'True'

    def printf(self):
        return 'Paper'
