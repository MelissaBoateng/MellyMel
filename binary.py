import random
import time

def binarySearch(sequence, target):# function that divides sorted array into two sub arrays to find target
    low= 0 #lowest starting index
    high = len(sequence)-1 #end point
    found = False #initilzing the find as false 
    while low<= high and not found:
        midpoint = (low + high)//2 #binary search formula for finding middle value
        if sequence[midpoint] == target: #if midpoint has index that represents the target number return true
            found = True
        else:
            if target < sequence[midpoint]:#if the target number less than midpoint index then we can find the corresponding number the right side of sub array
                high = midpoint-1
            else:
                low = midpoint+1
    return found
print("Binary search for N=100")
TimeInterval=[]
for i in range(1,6):#since we are finding time interval for N using the randomized sequence of numbers
    startTime=time.time()#initializing start time
    testlist = random.sample(range(1,32767),100)#randomizer to randomize the numbers with a size of 100 in the range 1,32767
    Newlist=sorted(testlist)#if the list isn't sorted the code would not run
    print(Newlist)
    X= int(input("enter number: "))#ask for user input
    print(binarySearch(Newlist,X))#print the index of the number if found return true if not false
    endTime= time.time()#find end time
    Interval=(endTime-startTime)*1000 #find interval in msecs
    TimeInterval.append(Interval) #for all 5 trials append their time interval into a list
print ("the average msecs after 5 trials for N=100 is: ",sum(TimeInterval)//5) #find the average of the times

'''
TimeInterval=[]
for i in range(1,6):
    startTime=time.time()
    testlist = random.sample(range(1,32767),1000)
    Newlist=sorted(testlist)
    print(Newlist)
    X= int(input("enter number: "))
    print(binarySearch(Newlist,X))
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
    print(binarySearch(Newlist,X))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    TimeInterval.append(Interval)
print (sum(TimeInterval)//5)




