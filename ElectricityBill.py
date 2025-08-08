inp = int(input("Enter the amount of units of electricity you used \n"))
bill = 0
tax = 0

if inp < 50:
    bill = inp * 2.60
    tax = 25
elif 100 > inp >= 50:
    bill = inp * 3.25
    tax = 35
elif 200 > inp >= 100:
    bill = inp * 5.26
else:
    bill = inp * 8.45
    tax = 75

total = float(bill + tax)
print("Total Electricity Bill Is:",total)