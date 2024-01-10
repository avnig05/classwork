'''
Avni Gandhi
CIS 41A Spring 2023
Unit B, Exercise B
'''

#string methods
name = input("Please enter a name: ")
print(name.upper())
print(len(name))
print(name[3])
name2 = name.replace("o", "x")
print(name2)
print(name)

#counting and finding (FIX THIS)
quote = "Believe you can and you're halfway there"
print("Count =", quote.count('a'))
pos = quote.find('a')
while pos > -1:
    print("a is found at  ", pos)
    pos = quote.find('a', pos+1)

'''
Execution results:
Please enter a name: George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
Count = 4
a is found at   13
a is found at   16
a is found at   28
a is found at   32
'''
