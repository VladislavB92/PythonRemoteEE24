print("Hello! This is a simple calculator")
continue_calculation = "y"

while continue_calculation == "y":
    while True:
        first_number = input("Enter first number: ")
        if "," in first_number:
            print("Please use '.' for numbers")
        elif not first_number.replace(",", "", 1).isdigit():
            print("Please enter a valid number what does't have coma")
        else:
            break

    while True:
        operator = input("+ , - , * , / : ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Enter correct operator")
    operator = operator[0]

    while True:
        second_number = input("Enter second number: ")
        if "," in second_number:
            print("Please use '.' for numbers")
        elif not second_number.replace(",", "", 1).isdigit():
            print("Please enter a valid number")
        else:
            if operator == "/" and float(second_number) == 0:
                print("You can't devide wit 0, try again")

        break

    if operator == "+":
        operation_result = float(first_number) + float(second_number)
    elif operator == "-":
        operation_result = float(first_number) - float(second_number)
    elif operator == "*":
        operation_result = float(first_number) * float(second_number)
    elif operator == "/":
        operation_result = float(first_number) / float(second_number)

    else:
        exit("Try again")

    operation_result: float = round(operation_result, 2)

    result: str = f"{first_number} {operator} {second_number} = {operation_result}"

    print(result)

    print("Do you want to calculate sometging else?")
    continue_calculation = input("y/n: ")

print("Bye!")