# Tip Calculator Program
print("Welcome to the tip calculator.")

bill = float(input("What is the total bill? "))
tip = int(input("Enter the tip percentage: "))
people = int(input("How many people are splitting the bill? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = round(bill + total_tip, 2)
bill_split = round(total_bill / people, 2)


print(f"The total bill is {total_bill}")
print(f"Each person should pay {bill_split}")