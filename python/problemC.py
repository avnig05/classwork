'''
Avni Gandhi
CIS 41A, Spring 2023
Unit C, Problem C
'''

#working with lists
list1 = []
list1 = [1,3,5]
temp = list1[2]
list1[2] = list1[1]
list1[1] = temp
print("Items in list1:")
for i in range(0, len(list1), 1):
    print(list1[i])

list2 = [1,2,3,4]
list3 = list1 + list2
print("list3 is:",list3)

print("list3 contains a 3:", 3 in list3)
print("list3 contains", list3.count(3), "3s")
print("the first index of the first 3 contained in list3 is", list3.index(3))

first3 = list3.pop(2)
print("first3 =", first3)
list4 = sorted(list3)
print("list3 is now:", list3)
print("list4 is:", list4)
print("slice of list3 is:", list3[2:5])
print("length of list3 is", len(list3))
print("the max value in list3 is", max(list3))
list3.sort()
print("Sorted list3 is:", list3)
list5 = [list1, list2]
print("list5 is:", list5)
print("Value 4 from list5:", list5[1][3])

'''
Execution results:
Items in list1:
1
5
3
list3 is: [1, 5, 3, 1, 2, 3, 4]
list3 contains a 3: True
list3 contains 2 3s
the first index of the first 3 contained in list3 is 2
first3 = 3
list3 is now: [1, 5, 1, 2, 3, 4]
list4 is: [1, 1, 2, 3, 4, 5]
slice of list3 is: [1, 2, 3]
length of list3 is 6
the max value in list3 is 5
Sorted list3 is: [1, 1, 2, 3, 4, 5]
list5 is: [[1, 5, 3], [1, 2, 3, 4]]
Value 4 from list5: 4
'''


