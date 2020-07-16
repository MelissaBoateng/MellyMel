'''Question 1: DotProduct '''
'''This function generates a random sample from a given range of values N and calculates their dotproduct'''
'''The function takes the sum of the assigned list and for each element of the list performs a multiplication'''
from random import sample
import math

def Dotproduct(N,ListA,ListB):
    Dotproduct=[x*y for x,y in zip(ListA,ListB)] '''the use of zip is to pair each item in a tuple with their corresponding item in the other tuple'''
    DP= sum(Dotproduct)
    print(DP)
