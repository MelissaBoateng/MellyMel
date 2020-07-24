'''
Given a sorted array of N uniformly distributed values Arr[], write a function to search for a particular element target, in the array
index = low + [(target-arr[low])*(high-low) / (arr[high]-arr[low])]
arr= sorted array
target= number being looked for from the area
Pos= the index that most suitably identifies the target number
low= starting index of sorted array
high= index of value at rear of the array
'''

def InterpolationSearch(arr, target):#the function takes two inputs, array and the number we are looking for
   low = 0 #the lowest value starts at index 0
    high = (len(arr) - 1) #the highest value is calculated as the lenght of the array-1
    while low <= high and target >= arr[low] and target<= arr[high]:# while the target is in the sorted array
        index = low + int(((float(high - low) / ( arr[high] - arr[low])) * ( target- arr[low]))) #Formula for finding the index using interpolation by estimating the mid
        if arr[index] == target:# (key value is found)a target is reached when the index of the input array matches with the target number and python goes on to return that index 
            return index
        elif arr[index] < target:#for every inputted target, if the value of the target is greater than the index of the target value of the array, python does a re-evaluation using the left part formula of the sub array
            low = index + 1; #the lowest value then becomes the found index plus one
        else:
            high = index - 1;# else #for every inputted target, if the value of the target is less than the index of the target value of the array, python does a re-evaluation using the right part formula of the sub array
    return -1 #return -1 if the target doesn't exist
