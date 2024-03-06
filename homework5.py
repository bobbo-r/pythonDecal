#P1 Find element with identitcal entries
import numpy as np

a = np.array([[1, 2, 3], [1, 1, 1], [2, 1, 1]])
#a = np.append(a, [value], axis=0)
print(a)
"""print(a[1])
print(len(np.unique(a[0])))
print(len(np.unique(a[1])))
print(len(np.unique(a[2])))
"""

def equal(a):
    result = np.array([()])
    b=0
    for i in range(len(a)):
        if len(np.unique(a[i]))==1:
            desired_row = np.array([a[i]])
            result = np.append(desired_row, [desired_row[b]], axis=0)
            b+=1
            
    return result

print(equal(a))

    


