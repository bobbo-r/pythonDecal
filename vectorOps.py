"""
IMPORTANT NOTES:

https://www.geeksforgeeks.org/taking-input-from-console-in-python/

^ Input commmands and examples
    # input() reads from command line
    # int(input()) input converted to integer value

Function of this: make many functions to help with my math 54 homework

Imports: numpy, linalg to use inverse and other helpful functions 
Documentation: Numpy has linalg group (contains .dot, .multiply, .transpose....) and 
SciPy has linalg which has other functions

To run:
        -) open terminal
        -) type in user directory "python ./pythonDecal/vectorOps"

        Can also run from VS terminal
"""



import numpy as np
from numpy.linalg import inv

def inputMatrix():
    d=0
    while d<1:
        print("Welcome: Specify size of A: Row = ?")
        row = int(input()) #reads int of input
        print("\nColumn: ?")
        col = int(input())
        if row<=0 or col<=0: #valid dimensions
            return print("Oops! Invalid dimensions: must be positive nonzero integers...")
        print("\nBegin inputting, then hit return one number at a time row-wise.\n Then it will prompt you to start new row.\n\nExample: 2, 3, 4 >> [2, 3, 4].... >")
        print("\n******Row 1: >")
        A = np.empty((row,col))
        for i in range(row):
            for j in range(col):
                A[i][j] = int(input())
            if (i<row-1): print("\n******Row "+str(i+2)+": >")
        print("\n**********Enter b vector column-wise: ")
        b  = np.empty((col, 1))
        for i in range(col):
            b[i] = int(input())
        d = 1
    print("\nMatrix A: ")
    print(A)
    
    At = np.transpose(A)
    AtA = np.dot(At, A)
    if (inv(AtA)):
        AtAinv = inv(AtA)
    Atb = np.dot(At, b)
    x = np.dot(AtAinv, Atb)
    print(Atb)
    print(AtA)
    print(AtAinv)
    print("\n Least square sol'n x hat == ")
    return print(x)
print(inputMatrix())

"""

 #columns of first matrix = rows of second matrix

#Q = np.array([(1, -1, 9/2), (-1, 1, 3/2), (0, 2, 1), (1, 1, -9/2), (1, 1, 11/2)])
#Qt = np.transpose(Q)



AtAinv = inv(AtA) # if error: singular matrix = det=0 cant be inverted
print("AtA inv: ")
print(AtAinv)

def square(x):
    result = np.empty((len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j]**2
    return result
b = square(x)
def sum(b):
    for i in range()


"""

