'''
Avni Gandhi
CIS 41A, Spring 2023
Unit B, Problem B
'''


#First Script -- Working with Strings


#string type tests
string = input("Please enter a string: ")
print(string.isupper())
print(string.isdigit())
print(string.isalpha())

#escape characters within a string

haiku = "Type, type, type away. \nCompile. Run. Hip hip hooray! \nNo error today!"
print(haiku)


#slicing a string
quote = "And now for something completely different"
print(quote[0:6])
print(quote[38:42])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])

#using string operators
pattern1 = ".-*'"
pattern2 = pattern1 + pattern1[::-1]
print(pattern2 * 5)
print("\n")

#Second Script

#printing a well formatted invoice
smallPrice = 10.20
medPrice = 8.52
largePrice = 7.98

small = int(input("How many boxes of small beads do you need? "))
medium = int(input("How many boxes of medium beads do you need? "))
large = int(input("How many boxes of large beads do you need? "))

print("SIZE      QTY      COST PER BOX    TOTALS")
print("Small %7.0f %17.2f %9.2f" %(small, smallPrice, (small*smallPrice)))
print("Medium %6.0f %17.2f %9.2f" %(medium, medPrice, (medium*medPrice)))
print("Large %7.0f %17.2f %9.2f" %(large, largePrice, (large*largePrice)))
print("TOTAL %35.2f" %((small*smallPrice) + (medium*medPrice) + (large*largePrice)))

'''
Execution 1 Results:

Please enter a string: ABC123
True
False
False
Type, type, type away. 
Compile. Run. Hip hip hooray! 
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.-*''*-..-*''*-..-*''*-..-*''*-..-*''*-.


How many boxes of small beads do you need? 10
How many boxes of medium beads do you need? 9
How many boxes of large beads do you need? 8
SIZE      QTY      COST PER BOX    TOTALS
Small      10             10.20    102.00
Medium      9              8.52     76.68
Large       8              7.98     63.84
TOTAL                              242.52




Execution 2 Results:

Please enter a string: ABC123
True
False
False
Type, type, type away. 
Compile. Run. Hip hip hooray! 
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.-*''*-..-*''*-..-*''*-..-*''*-..-*''*-.


How many boxes of small beads do you need? 5
How many boxes of medium beads do you need? 10
How many boxes of large beads do you need? 15
SIZE      QTY      COST PER BOX    TOTALS
Small       5             10.20     51.00
Medium     10              8.52     85.20
Large      15              7.98    119.70
TOTAL                              255.90

'''


