# TODO: A better way to format long imports. Fixed.
from calcu_functions import (
	plus_operation,
	minus_operation,
	multiplication_operation,
	division_operation,
)

print("Hello! This is a simple calculator.")

while True:
	try:
		first_number = float(input("Enter first number: "))
	except ValueError:
		print("Invalid input! Please enter a valid number.")
		continue

	operator = input("+ - * / ")
	print(f"My chosen operator: {operator}")
	operator = operator[0]

	try:
		second_number = float(input("Enter second number: "))
	except ValueError:
		print("Invalid input! Please enter a valid number.")
		continue

	valid_second_number = False
	while not valid_second_number:
		if operator == "/" and second_number == 0:
			print("Error: Division by zero. Please try again.")
			try:
				second_number = float(input("Enter second number: "))
			except ValueError:
				print("Invalid input! Please enter a valid number.")
				continue
		else:
			valid_second_number = True

	operation_result = None

	if operator == "+":
		operation_result = plus_operation(first_number, second_number)
	elif operator == "-":
		operation_result = minus_operation(first_number, second_number)
	elif operator == "*":
		operation_result = multiplication_operation(first_number, second_number)
	elif operator == "/":
		operation_result = division_operation(first_number, second_number)

	# TODO: Can be done also as 'if operation_result and...', as we check if the value exists.
	if operation_result is not None and abs(operation_result - round(operation_result)) < 1e-10:
		operation_result = int(operation_result)

	if isinstance(operation_result, int):
		result = f"{operation_result}"
	else:
		# TODO: Missing whitespace after operation_result:
		result = f"{operation_result:.2f}"

	print(result)

	print("Do you want to calculate something else?")
	continue_calculation = input("y/n ")

	if continue_calculation.lower() != "y":
		break

print("Bye!")
