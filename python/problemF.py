'''
Avni Gandhi
CIS 41A, Spring 2023
Unit F, Problem F
'''
import random

def generate_invoice(unitPrice, quantity, shipping = 10, handling = 5):
    total = unitPrice * quantity
    grandtotal = total + shipping + handling

    invoice = f"Cost (unitPrice x quantity) = {total} \n"
    invoice += f"Shipping = {shipping} \n"
    invoice += f"Handling = {handling} \n"
    invoice += f"Total = {grandtotal} \n"

    return invoice

print()
def printGroupMembers(groupName, *studentNames):
    print("Members of", groupName)
    for i in studentNames:
        print(i)

print("\n")
def overseerSystem(**kwargs):
    if "temperature" in kwargs and kwargs["temperature"] > 500:
        print("Warning: temperature is", kwargs["temperature"])
    if "CO2level" in kwargs and kwargs["CO2level"] > 0.15:
        print("Warning: CO2level is", kwargs["CO2level"])
    if "miscError" in kwargs:
        print("Misc error #", kwargs["miscError"])

def out():
    print("Out")
    return 0
def single():
    print("Single")
    return 1
def double():
    print("Double")
    return 2
def triple():
    print("Triple")
    return 3
def homerun():
    print("Homerun")
    return 4


def main():
    print(generate_invoice(20, 4, shipping = 8))
    print(generate_invoice(15, 3, handling = 15))
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(*groupB)
    print()
    messages = [{"temperature":550},
                {"temperature" :475},
                {"temperature":450, "miscError":404},
                {"CO2level":.17},
                {"CO2level":.2, "miscError":418}]
    for i in messages:
        overseerSystem(**i)

    outcomes = [out, single, double, triple, homerun]
    probabilities = [70, 18, 5, 1, 6]

    outs = 0
    total = 0
    print()
    while outs < 3:
        outcome = random.choices(outcomes, weights = probabilities, k = 1)
        result = outcome[0]()
        if result > 0:
            total += result
        else:
            outs += 1
    print(f"Total Score: {total}")
    

if __name__ == "__main__":
    main()


'''
Execution results:
Cost (unitPrice x quantity) = 80 
Shipping = 8 
Handling = 5 
Total = 93 

Cost (unitPrice x quantity) = 45 
Shipping = 10 
Handling = 15 
Total = 70 

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

Warning: temperature is 550
Misc error # 404
Warning: CO2level is 0.17
Warning: CO2level is 0.2
Misc error # 418

Out
Out
Single
Homerun
Out
Total Score: 5
'''

    

