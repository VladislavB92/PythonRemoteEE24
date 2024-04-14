import cal5

print("Hello! This is a simple calculator.")
print("It can perform +, -, *, and / operations.")

while True:
    calculate_or_history: str = input("1 Calculate\n2 See history\n")

    if calculate_or_history == "1":
        first_number: int = int(input("Enter first number: "))
        operator: str = input("Enter the operation (+, -, *, /): ")
        second_number: int = int(input("Enter second number: "))

        if operator in ['+', '-', '*', '/']:
            if operator == "+":
                operation_result = cal5.add(first_number, second_number)
            elif operator == "-":
                operation_result = cal5.subtract(first_number, second_number)
            elif operator == "*":
                operation_result = cal5.multiply(first_number, second_number)
            elif operator == "/":
                try:
                    operation_result = cal5.divide(first_number, second_number)
                except ValueError as e:
                    operation_result = str(e)
        else:
            operation_result = "Wrong operator"

        result: str = f"{first_number} {operator} {second_number} = {operation_result}\n"
        print(result)

        with open("greeting.txt", "a") as greeting_file:
            greeting_file.write(result)

    elif calculate_or_history == "2":
        with open("greeting.txt", "r") as greeting_file:
            greetings = greeting_file.readlines()
            for line in greetings:
                print(line, end="")
    else:
        print("Invalid input, please try again.")

    continue_prompt: str = input("Do you want to continue? y/n ")
    if continue_prompt.lower() != "y":
        print("Good luck!")
        break