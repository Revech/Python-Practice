print("Welcome to Python Pizza Delivery")
size = input("What size of the pizza do you prefer? S,M, or L? ")
pepperoni = input("Do you want pepperoni pizza? Y/N ")
extra_cheese = input("Do you want extra cheese? Y/N ")

total = 0

if(size == 'S' or size == 's'):
    total +=10
elif(size == 'M' or size == 'm'):
    total += 15
else:
    total += 20
if(pepperoni == 'y' or pepperoni == 'Y'):
    total += 2
if(extra_cheese == 'y' or extra_cheese == 'Y'):
    total += 5
print(f"Your total amount is ${total}")



