bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? ₹"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
split_between_people = float(input("How many people to split the bill? "))

total_bill = bill+bill*tip_percent/100
price_per_person = total_bill/split_between_people

print(f"Each person should pay: ₹{round(price_per_person,2)}")
