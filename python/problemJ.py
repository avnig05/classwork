'''
Avni Gandhi
CIS 41A, Spring 2023
Problem J, Unit J
'''

import re

#part 1
data = input("Please enter some text: ")
pattern = r'a'
if re.search(pattern, data):
    print("Found")
else:
    print("Not Found")

#part 2
data = input("Please enter some text: ")
pattern = r'b\.'
print(re.findall(pattern, data))

#part 3
data = input("Please enter some text: ")
pattern = r' '
print(re.split(pattern, data))


#part 4
data = input("Please enter some text: ")
pattern = r'th'
print(re.sub(pattern, 'lore', data))

'''
Execution results:
Test 01
Please enter some text: Harry S. Truman
Found
Please enter some text: Dobby Rebeus Longbottom Gabrielle Albus
[]
Please enter some text: Bill Charlie Percy Fred George Ron Ginny
['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']
Please enter some text: thlei, th, and folk tales
lorelei, lore, and folk tales

Test 02
Please enter some text: Dwight D. Eisenhower
Not Found
Please enter some text: Dobby Rebeus Longbottom Gabrielle Albus
[]
Please enter some text: Bill Charlie Percy Fred George Ron Ginny
['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']
Please enter some text: thlei, th, and folk tales
lorelei, lore, and folk tales

'''
