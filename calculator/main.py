from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    print(logo)

    num1 = float(input("What's the first number?: "))

    continue_calculating = True

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        if (
            input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            num1 = result
        else:
            calculate()


calculate()
