#In class 3/4/24
#Comm+T and >select Interpretter, choose  (base)

import numpy as np
import time #allows use of time library

def function(num):
    return num**2   #Num squared

def loop_speedtest(n):
    start = time.time()  # time.time() function
    result = list(range(n)) #makes a list from 0 to n
    for i in result:
        result[i] = function(result[i])  #squares every element in result
    end  = time.time() # takes end time
    return end-start

def numpy_speedtest(n):
    start = time.time()  # time.time() function
    result = np.arange(n) #makes a list from 0 to n, in np
    result = function(result)  #reevalutes result
    #at every element in result DONT HAVE TO USE FOR LOOP
    end  = time.time() # takes end time
    return end-start #duration used

reps = 1000
print(loop_speedtest(reps))
print(numpy_speedtest(reps))

"""
RESULT: on average, numpy is FASTER
"""

#Find unique elements in an array and the number of each element
nums = np.array([(1, 2, 3, 5, 2, 3, 1)])
def uniqueEle(nums):
    nums = np.unique(nums, return_counts = True) #check documentation
    return nums
print(uniqueEle(nums))

## Given 2D array, find mean of columns, replace
##each element less than the col's mean with the mean

"""
([34, 37, 29], [1, 36, 41], [37, 34, 29], [1, 49, 14])
"""
arr = np.array([(34, 37, 29), (1, 36, 41), (37, 34, 29), (1, 49, 14)])
means = np.mean(arr, axis = 0) # for multidim arrays, can
#specify axis ex) axis(0) is along columns (one axis)
#axis(1) = along row
#3d array = axis(2) is along a different axis

print(means)
for i in range(arr.shape[1]): # number of columns
    arr[:, i][arr[:, i] < means[i]] = means[i] # anything in column less than the mean set = to mean at position i
    #all rows, i'th column
