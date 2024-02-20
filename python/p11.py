# p11.py
# Avni Gandhi
# 1/22/2023
# Python 3.11.1
# Description: A program to simulate rock-paper-scissors game.

# need this for randint()
import random

#ask user for input
p1 = int(input('Player 1 enter 1 for rock, 2 for paper, 3 for scissors:'))
p2 = int(input('Player 2 enter 1 for rock, 2 for paper, 3 for scissors:'))

# show the generated values
print('PLayer 1 =', p1)
print('Player 2 =', p2)

# make variables to store values for rock paper scissors
rock = 1
paper = 2
scissors = 3

# 3 cases when p1 wins
if p1 == rock and p2 == scissors:
    print("Player 1 wins, rock breaks scissors!")
elif p1 == paper and p2 == rock:
    print("PLayer 1 wins, paper covers rock!")
elif p1 == scissors and p2 == paper:
    print ("Player 1 wins, scissors cut paper!")

#3 cases when p2 wins
if p2 == rock and p1 == scissors:
    print("Player 2 wins, rock breaks scissors!")
elif p2 == paper and p1 == rock:
    print("Player 2 wins, paper covers rock!")
elif p2 == scissors and p1 == paper:
    print("PLayer 2 wins, scissors cut paper!")

#3 cases when p2 and p1 tie
if p2 == rock and p1 == rock:
    print("tie")
if p2 == paper and p1 == paper:
    print("tie")
if p2 == scissors and p1 == scissors:
    print("tie")

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p11.py ===================
Player 1 enter 1 for rock, 2 for paper, 3 for scissors:3
Player 2 enter 1 for rock, 2 for paper, 3 for scissors:2
PLayer 1 = 3
Player 2 = 2
Player 1 wins, scissors cut paper!
>>>
'''

