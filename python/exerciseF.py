'''
Avni Gandhi
CIS 41A, Spring 2023
Unit F, Exercise F
'''

#part one
def hello():
    '''This function prints Hello World'''
    print("Hello World")

def printListElement(element, index):
    try:
        print(element[index])
    except IndexError:
        print("Error: bad index number.")
    print()

def byVal(param):
    print("Original ID of parameter in byVal", id(param))
    param += 7
    print("ID of parameter in byVal after change", id(param))

def byRef(param):
    print("Original ID of parameter in byRef", id(param))
    print("Original ID of parameter's last element in byRef", id(param[-1]))
    param[-1] += 7
    print("ID of parameter in byRef after change", id(param))
    print("ID of parameter's last element in byRef after change", id(param[-1]))


def main():
    hello()
    help(hello)
    myInt = 3
    myList = list(range(3))
    printListElement(myList, 3)
    print("Original ID of myInt in main is", id(myInt))
    print("Original ID of myList in main is", id(myList))
    print("Original ID of myList's last element in main is", id(myList[-1]))
    byVal(myInt)
    byRef(myList)
    print("ID of myInt in main after call to byVal is", id(myInt))
    print("ID of myList in main after call to byRef is", id(myList))
    print("ID of myList's last element in main after call to byRef is", id(myList[-1]))
    print("myInt is now:", myInt)
    print("myList is now:", myList)

if __name__ == '__main__':
    main()

'''
Execution results:
Hello World
Help on function hello in module __main__:

hello()
    This function prints Hello World

Error: bad index number.

Original ID of myInt in main is 4416552376
Original ID of myList in main is 4398142976
Original ID of myList's last element in main is 4416552344
Original ID of parameter in byVal 4416552376
ID of parameter in byVal after change 4416552600
Original ID of parameter in byRef 4398142976
Original ID of parameter's last element in byRef 4416552344
ID of parameter in byRef after change 4398142976
ID of parameter's last element in byRef after change 4416552568
ID of myInt in main after call to byVal is 4416552376
ID of myList in main after call to byRef is 4398142976
ID of myList's last element in main after call to byRef is 4416552568
myInt is now: 3
myList is now: [0, 1, 9]
'''
