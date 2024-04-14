from functions import plus_operation, minus_operation, multiply_operation, divide_operation

print("Hello! This is a simple calculator.")
print("It performs basic mathematical operations")

continue_calculation = "y"
while continue_calculation == "y":

	number_1 = input("Please enter the first number: ")
	operator: str = input("enter the mathematical operation to run: ")
	number_2 = input("Please enter the second number: ")

	if operator == "+":
		operation_result = plus_operation(number_1, number_2)

	elif operator == "-":
		operation_result = minus_operation(number_1, number_2)

	elif operator == "*":
		operation_result = multiply_operation(number_1, number_2)

	elif operator == "/":
		operation_result = divide_operation(number_1, number_2)

	else:
		print("this calculator doesn't recognize the operation. Please enter a valid one!")
		continue

	# result: str = f"{number_1} {operator} {number_2} = {operation_result:.2f}"
	# operation_result: float = round(operation_result, 2)

	result: str = f"{number_1} {operator} {number_2} = {operation_result}"
	operation_result: int(operation_result)

	with open("greeting.txt", "a") as greeting_file:
		greeting = greeting_file.write(f"{str(result)}\n")

	# with open("greeting.txt", "r") as greeting_file:
	#     greetings = greeting_file.readlines()
	#     for line in greetings:
	#         print(line)

	# operation_result_int: float = round(operation_result, 2)
	# result: str = f"{first_number} {operator} {second_number} = {operation_result:.2f}"

	# result: str = f"{first_number} {operator} {second_number} = {round(operation_result, 2)}"

	print(result)

	print("Do you want to continue?y/n")
	continue_calculation = input("y/n")
	print("bye!")
