#P1 Find element with identitcal entries
import numpy as np

a = np.array([(1, 2, 3), (1, 1, 1), (2, 2, 2)])
a = np.append([(1,2, 3)], 1)
print(a)

def equal (a):
    result = np.array([])
    for i in range(len(a)):
        if a[i][i]==a[i][i]:
            result = np.append(a[i])
    return result

print(equal(a))

    


