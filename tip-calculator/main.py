def convert_to_float(input):
    try:
        return float(input)
    except ValueError:
        pass


print("Welcome to the tip calculator!")
bill = convert_to_float(input("What was the total bill? $"))
tip_percentage = convert_to_float(
    input("How much tip would you like to give? 10, 12, or 15? ")
)
people = convert_to_float(input("How many people to split the bill? "))

if bill != None and tip_percentage != None and people != None:
    bill_per_person = "{:.2f}".format(
        round(bill / people * (1 + tip_percentage / 100), 2)
    )
    print(f"Each person should pay: ${bill_per_person}")
