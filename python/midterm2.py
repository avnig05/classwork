for num in range(5,3, -1):
    print(num)


list1 = [1,2,10,65,42,78,90,11,34,64,23,43]

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}

x = class1.intersection(class2) - class3
print(x)

for num in range(2, 21, 2):
    if(num % 2 == 0):
        print(num)

def priceGuide(avgPrice):
    if avgPrice <= 10:
        print("Inexpensive")
    elif avgPrice <= 30:
        print("Moderate")
    else:
        print("Pricey")

priceGuide(18)
priceGuide(2)
priceGuide(90)

