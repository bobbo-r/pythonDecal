#P1
a = []

for i in range (51):
    a.append(i)
#print(a)

#no errors

#P2
nums = [1, 2, 3]

def square (nums):
    squarelist = []
    for i in range (len(nums)):
        squareNum = nums[i]*nums[i]
        squarelist.append(squareNum)
    return squarelist
#print(square(nums))

"""
error 1: prints empty list
changed line 15 incorrect name for "squarelist" -> no change
error fixed: print function instead of initially defined empty list
Output: [1, 4, 9]
"""

#P3
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def odd(listA, listB):
    oddList = []
    for i in range (0, len(listA), 2):
        oddList.append(listA[i])
    for i in range (0, len(listB), 2):
        oddList.append(listB[i])
    return oddList
#print(odd(listA, listB))
"""
errors:
    returns scalar
        fix: oddList.append() added instead of oddList = list[i]
    returns even numbers
        fix: index start change from 1 to 0
"""
#P3.1
import numpy as np
matrix = np.zeros((5, 5))
entry = 1
for i in range(5):
    for j in range(5):
        matrix[i, j]=entry
        entry += 1
 
#print(matrix)

"""
errors: outputted matrix of all zeros
    fixed: original line 53 entry = matrix[i,j], fixed to matrix = entry
"""

#P3.2
M = np.empty((5, 5), dtype=object)

entry = 1
for i in range(5):
    for j in range(5):
        M[i, j]=entry
        entry+=1
for i in range(5):
    for j in range(5):
        if M[i, j]%3==0:
            M[i, j]='?'

print('\n')
print(M)
print('\n')

"""
errors:
    Value error, string not convertable to float in line 74
    fix: changing M to a matrix of type "Object" allowed ANY
    value to be in the indice [i, j]
    normally, numpy.empty(size, dtype) dtype is float by default
"""
#P4
old = [1, 2, 3, 4, 4, 5]
def duplicate(old):
    a=[]
    for i in range (len(old)):
        if old[i]==old[i-1]:
            a.append(old[i])
    return a
print(duplicate(old))


            



    
