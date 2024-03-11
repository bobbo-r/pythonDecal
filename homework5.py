#P1 Find element with identitcal entries
import numpy as np

a = np.array([[1, 2, 3], [1, 1, 1], [2, 1, 1], [3, 3, 3]])
#a = np.append(a, [value], axis=0)


def equal(a):
    b=0
    result = np.array([()])
    for i in range(len(a)):
        if len(np.unique(a[i]))==1:
            desired_row = np.array([a[i]])
            result = np.append(result, [desired_row[0]])
            b+=1
            
    return result

print(equal(a))

    
#P2
#np.zeros((row, col), dtype, order type (row or column storage), *, like)
def checker():
    result = np.zeros((8, 8))
    odd = np.array([(1, 0, 1, 0, 1, 0, 1, 0)])
    even = np.array([(0, 1, 0, 1, 0, 1, 0, 1)])
    for i in range(0, 8):
        if i%2==0:
            result[i] = odd[0]
        else:
            result[i]=even[0]
    return result

print(checker())

#P3
strings = np.array([('beans'), ('rice'), ('lettuce')])
#print(strings)
#print(np.array([(strings[1])]))
#"""
def spaces(strings):
    result = np.empty((1, len(strings)), dtype=object)
    for i in range(len(strings)):
        word = strings[i]
        newWord = ''
        for j in range(len(strings[i])):
            if j!=(len(word)-1):
                newWord += word[j]
                newWord += ' '
            else:
                newWord +=word[j]
            
        result[0][i]= newWord
    return result

print(spaces(strings))
    
#"""

#P4
np.random.seed(12345)
a = np.random.randint(1, 50, (4,5))
print(a)

def sortCol(a):
    b = np.sort(a, axis=0)      
    return b
print(sortCol(a))
