import random
class Deque:#hybrid data structure i.e double ended queue
    def __init__(self,sequence,sequenceSize,Maxsize): #initialize a deque data structure  
        if len(array)>arrayLength:
            return error
        self.sequence=sequence
        self.sequenceSize=sequenceSize
        self.Maxsize=sequenceSize
    def SeqEmpty(self):#sees if the deque is empty or full return true if true and false if otherwise
        return len(self.sequence)==0
    def SeqFull(self):
        return len(self.array)==self.length
    def SeqLength(self):#returns the number of elements currently in the deque
        return len(self.Maxsize)
    def add_To_Front(self,x):
        self.sequence.insert(0,x)
    def add_To_Back(self,x):
        self.sequence.append(x)
    def remove_From_Front(self):
        if self.SeqEmpty():
            raise EmptyDequeError("removeFront: removing from an empty deque:")#removes an item from the back of a sequence raises an error if deque is empty if not, return removed item
        self.sequence.pop(0)
    def remove_From_Back(self):
        if self.SeqEmpty():
            raise EmptyDequeError("removeBack: removing from an empty deque:")#removes an item from the back of a sequence raises an error if deque is empty if not, return removed item
        self.sequence.pop()
def SemiFull(s):    
    SemiFull=list(range(rand.randint(1,100)//2))
        
if __name__= __main__:
    q= Deque()
    q.add_To_Front(1)

