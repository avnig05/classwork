#Avni Gandhi
#2/12/2023
#Python 3.11.1
#Description: a dice game program that generates two random dice values.
#The user gets to roll as many times as they like while the computer can
#only roll once.

import random
randNum = random.randint(1,6)

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("You rolled ", dice1, "and", dice2)
    keep = input("Would you like to keep those? (y or n)")
    if(keep == 'y'):
        break

dice3 = random.randint(1,6)
dice4 = random.randint(1,6)

if ((dice1 + dice2) > (dice3 + dice4)):
    print("You win!")
if ((dice1 + dice2) < (dice3 + dice4)):
    print("You lose.")
if ((dice1 + dice2) == (dice3 + dice4)):
    print("It's a tie!")

print("The computer rolled a", dice3, "and", dice4)

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p22.py ===================
You rolled  5 and 3
Would you like to keep those? (y or n)n
You rolled  3 and 2
Would you like to keep those? (y or n)n
You rolled  2 and 6
Would you like to keep those? (y or n)y
You win!
The computer rolled a 5 and 2
>>>
'''
