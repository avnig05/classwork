#Avni Gandhi
#2/14/2023
#Python 3.11.1
#Description: a program that generates X random integers Num.

import random

X = random.randint(10,15)
total = 0

print("Generating", X, "random numbers")

for i in range(0, X, 1):
    num = random.randint(20,50)
    print(num)
    total += num
    if i == 0:
        smallestNum = num
        largestNum = num
    else:
        if num < smallestNum:
            smallestNum = num
        if num > largestNum:
            largestNum = num
            
    

print("Sum =", total)
print("Average = %.2f" %(total/X))
print("Smallest =", smallestNum)
print("Largest =", largestNum)


'''
>>>
=================== RESTART: /Users/avnigandhi/python/p24.py ===================
Generating 11 random numbers
28
39
32
33
30
49
46
31
47
32
26
Sum = 393
Average = 35.73
Smallest = 26
Largest = 49
>>>
'''
