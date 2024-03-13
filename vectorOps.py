import numpy as np
from numpy.linalg import inv

# input() reads from command line

d=0

while d<1:
    print("Welcome: Specify size of A: Row = ?")
    row = input()
    print("\nColumn: ?")
    col = input()
    print("\nBegin inputting, then hit return one number at a time row-wise.\n Then it will prompt you to start new row. >")
    print("\n******Row 1: >")
    A = np.empty((row,col))
    for i in range(len(row)):
        for j in range(len(col)):
            A[i][j] = input()
        print("\n******Row "+str(i+2)+": >")
    d = 1
print(A)

A = np.array([(2, 1, 1), (-2, 0, 1), (2, 3, 2)]) #columns of first matrix = rows of second matrix
print(A)
b = np.array([[-5],[8],[1]]) #coluimn vector
print(b)

At = np.transpose(A)
Q = np.array([(1, -1, 9/2), (-1, 1, 3/2), (0, 2, 1), (1, 1, -9/2), (1, 1, 11/2)])
Qt = np.transpose(Q)
AtA = np.dot(At, A)
print(AtA)
Ab = np.dot(A,b)
AtAinv = inv(AtA) # if error: singular matrix = det=0 cant be inverted
print("AtA inv: ")
print(AtAinv)



"""
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

