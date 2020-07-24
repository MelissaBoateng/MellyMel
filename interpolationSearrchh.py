# Python program to implement interpolation search 


# index of it, else returns -1
import random
import time
def InterpolationSearch(seq, N, x): # If x is present in sequence[0..n-1], then returns index of it, else returns -1
    low= 0
    high = (N - 1) 

    
    while low <= high and x >= seq[low] and x <= seq[high]: #using a sorted array, the elements in the sequence are defined in a range
        if low == high: 
            if seq[low] == x: 
                return low; 
            return -1; 
        
       
        index = low + int(((float(high - low) /
            ( seq[high] - seq[low])) * ( x - seq[low])))  # finding the index of a uniformly distributed sequence 


        
        if seq[index] == x:  # if target is found it is based on this Condition
            return True 

        
        if seq[index] < x: # If x is larger, x is in right part of the sub-array
            low = index + 1; 

        
        else:  # If x is smaller, x is in right part of the sub array
            high = index - 1; 
    
    return False# return this if number/target isn't in the sequence

print("for N=100:")
TimeInterval=[] #since we are finding time interval for N using the randomized sequence of numbers
for i in range(1,6):#the number of trials is 5 i.e 6-1= 5 
    startTime=time.time() #initializing start time
    testlist = random.sample(range(1,32767),100) #randomizer to randomize the numbers with a size of 100 in the range 1,32767
    Newlist=sorted(testlist) #if the list isn't sorted the code would not run
    print(Newlist)
    X= int(input("enter number: ")) #ask for user input
    print(InterpolationSearch(Newlist,100,X)) #print the index of the number if found return true if not false
    endTime= time.time() #find end time for finding if true or false
    Interval=(endTime-startTime)*1000 #expressing time in msecs
    TimeInterval.append(Interval)
print ("the average msecs after 5 trials for N=100 is: ",sum(TimeInterval)//5)

'''
print("for N=100:")

TimeInterval=[]
for i in range(1,6):
    startTime=time.time()
    testlist = random.sample(range(1,32767),1000)
    Newlist=sorted(testlist)
    print(Newlist)
    X= int(input("enter number: "))
    print(InterpolationSearch(Newlist,1000,X))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    TimeInterval.append(Interval)
print (sum(TimeInterval)//5)
'''
TimeInterval=[]
for i in range(1,6):
    startTime=time.time()
    testlist = random.sample(range(1,32767),5000)
    Newlist=sorted(testlist)
    print(Newlist)
    X= int(input("enter number: "))
    print(InterpolationSearch(Newlist,5000,X))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    TimeInterval.append(Interval)
print (sum(TimeInterval)//5)




