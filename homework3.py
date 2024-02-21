# 
#P1
print('\n Problem One: \n')
#set base x to the power of y
x=100
y=2
#pass power function the base and power
def power(x, y):
    c=x #used to track initial x
    i=1
    while i<y:
        #set x equal to itself times itself and iterate
        x=x*x
        i+=1
    print(str(c) + ' to the power of '+ str(y)+' is: '+str(x))
power(x, y) #calls power function with above x and y

print ('\n Problem 2: \n') #P2

#define list of ints
myNums = [-1, 500, 100, -1000]
#define function to find max
def maximum(myNums):
    m = myNums[0] #if no greater values, choose 1st value
    for i in range(1, len(myNums)+1): #iterate through list indices (need +1 because ending index is not included)
        if (myNums[i-1]>m): #if prior value > current value
            # update m to prior value
            m=myNums[i-1]
    return m
def minimum(myNums):
    mini=myNums[0] #sets minimum variable to first element
    for i in range(1, len(myNums)+1):
        if(myNums[i-1]<mini): # if element before smalle than current mini, set mini to that value and iterate through length of myNums
            mini=myNums[i-1]
    return mini
myTuple=(maximum(myNums), minimum(myNums)) #creates tuple max,min
print('List: '+str(myNums)+' has (max, min)= '+str(myTuple)) #prints result

print('\n Problem 3\n') #P3
year=24
def leapYear(year):
    if((year%4)!=0):
        return False
    elif(((year%100)!=0)&((year%400)!=0)):
        return False
    else:
        return True
#print the output
print('The year '+str(year)+' is a leap year: '+str(leapYear(year)))

print('\nProblem 4\n') #P4
#BMI for english system: ((lb)/[(inch)^2])*703
weight=180
height=74
def BMI(weight, height):
    BMI=(weight/(height*height))*703 #define BMI as value of formula
    return BMI
print('Weight(lb): '+str(weight)+' Height(inch): '+str(height)+' => BMI: '+str(BMI(weight, height)))

print('\nProblem 5\n')#P5
digits=10 #only for digits so integers
a=1 #defines a and b so they can be updated and printed outside function
b=1
def rotate_digits(digits):
    if(digits<10 and digits>-10): #if only a single digit, return the digit
        return digits
    else:
        a= digits%10 #returns the last digit in digits
        b= digits//10 #returns all other digits in digits
        rotated=str(a)+str(b) #writing last digit in front of others
        return rotated
    
print(rotate_digits(digits))

print('\nProblem 6\n')#P6
list = [1000, -2, 110, 4]
max=0
print('Maxes:')
def Max1(max, list): #Max: uses for loop
    for i in range (0, len(list)):
        if(list[i]>max):
            max=list[i]
    return max
print(Max1(max, list))
def Max2(max, list): #Max: uses while loop
    i=0
    while i<len(list):
        if(list[i]>max):
            max=list[i]
        i+=1 #increases i by 1, sets it equal to that value to iterate through list
    return max
print(Max2(max, list))
min=0
print('Mins:')
def Min1(min, list): #Min: uses for loop
    for i in range (0, len(list)):
        if(list[i]<min):
            min=list[i]
    return min
print(Min1(min, list))
def Min2(min, list): #Min: uses while loop
    i=0
    while i<len(list):
        if(list[i]<min):
            min=list[i]
        i+=1 #increases i by 1, sets it equal to that value to iterate through list
    return min
print(Min2(min, list))

print('\nProblem 7\n')#P7
phrase="UC BerkeleyaaaaA0#." #special, integer and non-vowel characters shouldn't change the count = true
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count=0
def vowelCount(phrase, vowels, count):
    for i in range(0, len(phrase)):
        for j in range(0, len(vowels)): 
            if(phrase[i]==vowels[j]):
                count+=1
    return count
print(vowelCount(phrase, vowels, count))

print('\nProblem 8\n') #P8

int=12345
sum=0
def digitalRoot(int, sum):
    a=str(int)
    b=len(a)
    for i in range(0, b):
        sum+=(ord(a[i])-ord('0')) #ord() turns a char into int
        #value of '0' is 48 (ASCII)
        #'1' is 49 and so forth
    return sum    
print(digitalRoot(int, sum))






    
        












    




    
    



    








