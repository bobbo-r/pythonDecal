"""
*** Numpy -> <import numpy as np> good for beginner
check slides


*** install : pip install numpy
or... conda install numpy 

arr = np.array([]) more powerful list
    can store any data type

    normally adding two lists conjoins them

    a = [1, 2] b=[3, 0] a+b = [1, 2, 3, 0]
    
adding two Numpy arrays adds components
    a+b = [4, 2]

takes add, subtract, multiply and divide by scalars

"""
import numpy as np

penis = np.array([2, 3, 5])
penis2 = np.array([3, 4, 5])
penis3 = penis + penis2
print(penis3)

#Add numbers one through 100 with for loop
penis4 = np.array([])
sum = 0
for i in range (0, 101):
    sum += i
print(sum)


"""do the same thing with np.arange(start, stop, step) creates 
array with ints 0 to end based on step value
np.sum() adds values of array together
"""
def arrayAdd():
    return np.sum(np.arange(0, 101))
print(arrayAdd())

"""
NP has mean, median, stat functions as well

2D arrays and Slicing:
arr = np.array([1, 2], [1, 2]....) >> each element is a row in matrix

indexed different then list
arr[row#, column#] or arr[row#, :] returns row vector arr[:, col#] returns column

arr[1:] everything after row arr[:1] everything after column

np. > max, min, sum. ones (array of ones with length),
 zeros (array of 0's), 
random.random( arrray random numbers of length provided)

"""





