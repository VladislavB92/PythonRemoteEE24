# TODO: Do not include brackets in the one line imports. Fixed.
from functions1 import (
	plus_operation,
	minus_operation,
	divide_operation,
	multiply_operation,
)


def input_number(prompt, allow_zero=True):
	while True:
		number = input(prompt)
		if not number.isnumeric():
			print("Please enter number!!!")
			continue
		if not allow_zero and float(number) == 0:
			print("zero not allowed")
			continue
		return float(number)


print("Hello! This is a simple calculator. Only for + - / and '")
continue_calculation = "y"
user_choice = None

while user_choice != "e":
	user_choice = input("Please choose - calculate - c, exit - e or history - h?: ")
	if user_choice == "h":
		with open("calculationHistory.txt", "r") as history_file:
			print(history_file.read())
		continue
	elif user_choice == "c":
		first_number = input_number("Enter first number: ")
		operator = input("Choose an operator, + - / *: ")
		operator = operator[0]
		print(f" operator: {operator}")
		second_number = input_number("Enter second number: ", operator != "/")

		if operator == "+":
			operation_result = plus_operation(first_number, second_number)
		elif operator == "-":
			operation_result = minus_operation(first_number, second_number)
		elif operator == "/":
			operation_result = divide_operation(first_number, second_number)
		elif operator == "*":
			operation_result = multiply_operation(first_number, second_number)
		else:
			print("are you... ???? Please enter valid operator")
			continue

		operation_result = round(operation_result, 2)
		result: str = f"{first_number} {operator} {second_number} = {operation_result}"
		print(result)

		# TODO: In Python, name files in snake case, NOT camelcase.
		with open("calculationHistory.txt", "a") as history_file:
			history_file.write(f"{result}\n")

print("Bye!")
