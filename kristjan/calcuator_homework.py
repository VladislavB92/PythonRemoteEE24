# TODO: The import line is too long. I will split it.
from functions_for_calculator_homework import (
	plus_operation,
	minus_operation,
	multiply_operation,
	divide_operation,
)

print("Hello! This is a simple calculator.")
continue_calculation = "y"

while continue_calculation.lower() == "y":

	while True:
		first_number = input("Enter first number: ")
		if first_number.replace(",", "", 1).isdigit():
			print("Yes, it is a digit.")
			break
		else:
			print("Please enter a valid number")

	while True:
		operator = input("Enter operator + , - , * , / :")
		if operator in ["+", "-", "*", "/"]:
			break
		else:
			print("Enter a valid operator")

	while True:
		second_number = input("Enter second number: ")
		if "," in second_number:
			print("Please insert '.' for numbers")
		elif not second_number.replace(",", "", 1).isdigit():
			print("Please enter a valid number")
		else:
			if operator == "/" and float(second_number) == 0:
				print("You can't divide with 0, please try again")
			else:
				break

	if operator == "+":
		operation_result = plus_operation(first_number, second_number)
	elif operator == "-":
		operation_result = minus_operation(first_number, second_number)
	elif operator == "*":
		operation_result = multiply_operation(first_number, second_number)
	elif operator == "/":
		operation_result = divide_operation(first_number, second_number)
	else:
		exit("Wrong operation, please try again")

	operation_result = round(operation_result, 2)

	if operation_result.is_integer():
		operation_result = int(operation_result)

	result = f"{first_number} {operator} {second_number} = {operation_result}"
	print(result)

	continue_calculation = input("Do you want to continue? (y/n): ")
	if continue_calculation.lower() != "y":
		break
# TODO: Why int("Bye")? What this meant for?
int("Bye")

print("Do you want to calculate something else? ")

continue_calculation = input("y/n: ")

print("Bye!")
