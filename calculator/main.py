from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("You should not divide by zero.")
        return 0


def calculate(previous_number):
    operator = input("Pick an operation: ")
    next_input = input("What's the next number?: ")
    next_number = float(next_input) if next_input.isdigit() else 0
    if operator in operations:
        result = operations[operator](previous_number, next_number)
        print(f"{previous_number} {operator} {next_number} = {result}")

        if (
            input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            ).lower()
            == "y"
        ):
            calculate(result)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


while True:
    print(logo)

    first_input = input("What's the first number?: ")
    first_number = float(first_input) if first_input.isdigit() else 0

    for item in operations:
        print(item)

    calculate(first_number)
