'''
Avni Gandhi
CIS 41A, Spring 2023
Unit A, Problem A
'''
import math
#basic numeric operations
a = 3 ** 2.5
print(a)
b = 2
b += 3
print(b)
c = 12
c /= 4
print(c)
d = 5 % 3
print(d)

#built-in functions abs, round, and min
print(abs(5-7))
print(round(3.14159, 4))
print(round(186282, -2))
numbers = [6,-9,-3,0]
print(min(numbers))

#functions from the math module
num = float(input("Please enter a number:"))
print("The square root of" , num ,"is %.2f" %math.sqrt(num))
print("The base-10 log of", num ,"is %.2f" %math.log(num, 10))

'''
15.588457268119896
5
3.0
2
2
3.1416
186300
-9
Please enter a number:7.6
The square root of 7.6 is 2.76
The base-10 log of 7.6 is 0.88
'''
