__author__ = 'sony'

#Rock class 
class Rock():
    nValue=1 #Value for Rock object is 1

    def cmp(self, other): #Cmp method to compare rock/paper/scissor
        nDiff=other.nValue-self.nValue
        if(nDiff%3==1):
            return 'False'
        if(nDiff==0):
            return 'Same'
        if(nDiff%3==2):
            return 'True'

    def printf(self):
        return 'Rock'
