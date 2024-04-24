print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = "{:.2f}".format(
    round((bill / people) * (1 + tip_percentage / 100), 2)
)
print(f"Each person should pay: ${bill_per_person}")
