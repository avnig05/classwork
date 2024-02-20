#Avni Gandhi
#2/4/2023
#Python 3.11.1
#Description: A program that displays the characters in the ASCII character
#from ! to ~

count = 0
asciiVal = 33 #max val is 126
for asciiVal in range(33, 127, 1):
    print(chr(asciiVal), end = ' ')
    count += 1
    if count == 10:
        print()
        count = 0
        
'''
>>>
=================== RESTART: /Users/avnigandhi/python/p18.py ===================
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~
>>>
'''
