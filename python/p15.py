#Avni Gandhi
#1/29/2023
#Python 3.11.1
#Description: A program that asks the user to enter 4 numbers
#(positive or negative) and finds the sum of all numbers,
#positive numbers, and negative numbers

#ask user to enter four numbers
num1 = float(input("enter number 1:"))
num2 = float(input("enter number 2:"))
num3 = float(input("enter number 3:"))
num4 = float(input("enter number 4:"))

#add all values together
sumAll = 0
sumAll = num1 + num2 + num3 + num4

#add all negative values together
sumNeg = 0
if num1 < 0:
    sumNeg = sumNeg + num1
if num2 < 0:
    sumNeg = sumNeg + num2
if num3 < 0:
    sumNeg = sumNeg + num3
if num4 < 0:
    sumNeg = sumNeg + num4

#add all positive values together
sumPos = 0
if num1 > 0:
    sumPos = sumPos + num1
if num2 > 0:
    sumPos = sumPos + num2
if num3 > 0:
    sumPos = sumPos + num3
if num4 > 0:
    sumPos = sumPos + num4

print("The sum of all numbers is", sumAll)
print("The sum of all negative numbers is", sumNeg)
print("The sum of all positive numbers is",sumPos)


'''
>>>
=================== RESTART: /Users/avnigandhi/python/p15.py ===================
enter number 1:-5
enter number 2:-2
enter number 3:7
enter number 4:2
The sum of all numbers is 2.0
The sum of all negative numbers is -7.0
The sum of all positive numbers is 9.0
>>>
'''
