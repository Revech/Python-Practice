print("Welcometo the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip percent would you like to give? 10, 12, or 15? "))
split_amount = int(input("how many people to split the bill?"))
150
12

total = ((total_bill * (tip / 100)) + total_bill) / split_amount


print(f"Each person should pay: ${round(total, 2)}")