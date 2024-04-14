# TODO: File names start always with a lowercase letter.


number_1 = int(input("Enter first number:"))

operator: str = input("+ ,- , * ,/:")

number_2 = int(input("Enter second number:"))

if operator == "+":
    plus_operation = (number_1 + number_2)
    print(plus_operation)


elif operator == "-":
    minus_operation = (number_1 - number_2)
    print(minus_operation)


elif operator == "*":
    multiply_operation = (number_1 * number_2)
    print(multiply_operation)


elif operator == "/":
    divide_operation = (number_1 / number_2)
    print(divide_operation)


else:
    print("invalid operator")

while True:
    number_1 = int(input("Enter first number: "))
    operator = input("Choose an operator (+, -, *, /) or 'quit' to exit: ")

    if operator == 'quit':
        print("Exiting calculator.")
        break

    number_2 = int(input("Enter second number: "))

    if operator == "+":
        result = number_1 + number_2
        print(f"Result: {result}")
    elif operator == "-":
        result = number_1 - number_2
        print(f"Result: {result}")
    elif operator == "*":
        result = number_1 * number_2
        print(f"Result: {result}")
    elif operator == "/":
        if number_2 != 0:
            result = number_1 / number_2
            print(f"Result: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operator!")

        # TODO: There is no result output or history.


