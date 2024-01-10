'''
Avni Gandhi
CIS 41A, Spring 2023
Unit E, Problem E
'''

import random
#script1
plantname = input("Please enter the plant name: ")
planttype = input("Please enter the plant type: ")
plantheight = int(input("Please enter the plant height: "))
if(planttype == 'Vegetable'):
    print("A", plantname, "can planted in the Vegetable garden.")
elif(planttype == 'Flower' and plantheight <= 3):
    print("A", plantname, "can be planted in the Low Garden or High Garden.")
elif(planttype == 'Flower' and (plantheight > 3 and plantheight <= 6)):
    print("A", plantname, "can be planted in the High Garden.")
else:
    print("A", plantname, "cannot be planted in any of the Gardens.")

#script2
secretNum = random.randint(1,100)
count = 1
print("Welcome to the guessing game.")
print("You need to guess a number from 1 to 100")
while True:
    guess = int(input("What is your guess? "))
    if (guess < secretNum):
        print("Guess is too low.")
    if(guess > secretNum):
        print("Guess is too high.")
    if (guess == secretNum):
        print("Congratulations!")
        break
    count += 1
print("You guess the secret number in" , count, "guesses.")


#script3
quote = "Believe you can and you're halfway there"
for i in range(0, len(quote)):
    if(quote[i] == 'a'):
        print("a found at index", i)

rows = int(input("Please enter the number of rows for the multiplication table: "))
for i in range(1, rows+1):
    for k in range(1, i+1):
           product = i * k
           print(f'{product:>2}' , end = ' ')
    print()
           
           

'''
Execution results:

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or High Garden.

Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai cannot be planted in any of the Gardens.

Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can planted in the Vegetable garden.

Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can planted in the Vegetable garden.

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden.

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower cannot be planted in any of the Gardens.


Welcome to the guessing game.
You need to guess a number from 1 to 100
What is your guess? 50
Guess is too high.
What is your guess? 30
Guess is too low.
What is your guess? 40
Guess is too high.
What is your guess? 35
Guess is too high.
What is your guess? 33
Guess is too low.
What is your guess? 34
Congratulations!
You guess the secret number in 6 guesses.


a found at index 13
a found at index 16
a found at index 28
a found at index 32


Please enter the number of rows for the multiplication table: 12
 1 
 2  4 
 3  6  9 
 4  8 12 16 
 5 10 15 20 25 
 6 12 18 24 30 36 
 7 14 21 28 35 42 49 
 8 16 24 32 40 48 56 64 
 9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
11 22 33 44 55 66 77 88 99 110 121 
12 24 36 48 60 72 84 96 108 120 132 144 

'''
