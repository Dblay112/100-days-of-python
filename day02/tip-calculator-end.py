print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15"))
people_split = int(input("How many people to split the bill? "))
tip_percent = percentage_tip / 100
total_tipamount = total_bill * tip_percent
t_bill = total_bill * total_tipamount
bpp = t_bill / people_split
final_am = round(bpp, 2)
print(f"Each person should pay: ${final_am}")
