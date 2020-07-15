'''Question 1: DotProduct '''
from random import sample
import math

def Dotproduct(N,ListA,ListB):
    Dotproduct=[x*y for x,y in zip(ListA,ListB)]
    DP= sum(Dotproduct)
    print(DP)