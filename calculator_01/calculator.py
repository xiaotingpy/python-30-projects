def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    print("Simple Calculator")
    print("Choose operation: +  -  *  /")

    operator = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Choose operation: +  -  *  /")

    try:
        operator = input("Enter operator: ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            print("Invalid operator")
            return

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")

