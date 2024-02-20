#Avni Gandhi
#2/4/2023
#Python 3.11.1
#Description: Program that reads in X whole numbers and outputs the sum of all
#positive numbers, negative numbers, and sum of all postive and negative
#numbers.

def main():
    numX = int(input('How many numbers would you like to enter?'))
    total = 0
    posTotal = 0
    negTotal = 0
    for index in range(0, numX, 1):
        number = float(input("Please enter number %i:" %(index+1)))
        total += number
        if number < 0:
            negTotal = negTotal + number
        if number > 0:
            posTotal = posTotal + number

    print("The sum of negative numbers =", negTotal)
    print("The sum of positive numbers =", posTotal)
    print("The sum of all numbers =" , total)
    repeat = input("Would you like to repeat? (y)(n):")
    if(repeat == 'y'):
        main()

if __name__ == "__main__":
    main()

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p20.py ===================
How many numbers would you like to enter?4
Please enter number 1:3
Please enter number 2:-4
Please enter number 3:-6
Please enter number 4:5
The sum of negative numbers = -10.0
The sum of positive numbers = 8.0
The sum of all numbers = -2.0
Would you like to repeat? (y)(n):n
>>>
'''
