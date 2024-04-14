# TODO: This line was too long. I have splited it.
from functions import (
	plus_operation,
	minus_operation,
	division_operation,
	multiplication_operation,
)

print("Hello! This is Victoria's very first simple calculator.")
print("It performs basic mathematical operations")
continue_calculation = "y"

while continue_calculation.lower() == "y":

	while True:
		first_number = input("Enter first number:")

		if first_number.replace(".", "", 1).isdigit():
			print("Yes, it is a digit")
			print("\n")
			break
		else:
			print("Please enter a valid number")
			print("\n")

	while True:
		operator = input("Enter operator (+, -, *, /):")
		if operator in ["+", "-", "*", "/"]:
			print("\n")
			break
		else:
			print("Please enter a valid operator")
			print("\n")

	while True:
		second_number = input("Enter second number:")
		if "," in second_number:
			print("Please use '.' for decimals")
		elif not second_number.replace(".", "", 1).isdigit():
			print("Please enter a valid number")
		else:
			if operator == "/" and float(second_number) == 0:
				print("You can't divide by zero. Please enter a valid number")
			else:
				break

	if operator == "+":
		operation_result = plus_operation(first_number, second_number)
	elif operator == "-":
		operation_result = minus_operation(first_number, second_number)
	elif operator == "*":
		operation_result = multiplication_operation(first_number, second_number)
	elif operator == "/":
		operation_result = division_operation(first_number, second_number)
	else:
		exit("Error, run once more")

	operation_result = round(operation_result, 2)

	if operation_result.is_integer():
		operation_result = int(operation_result)

	result = f"{first_number} {operator} {second_number} = {operation_result:}"
	print(result)

	with open("calculator_history.txt", "a") as calculator_history_file:
		calculator_history = calculator_history_file.write(f"{str(result)}\n")

	while True:
		# TODO: Better user experience would allow the user to enter just one character: y, n or h.
		#  Also, the code will be shorter as you will reference in the if/else statements only one letter.
		print("\nDo you want to continue calculation (yes), leave (no) or see the log (history) of it?")
		continue_calculation_or_see_history = input("(yes/no/history): ").lower()

		if continue_calculation_or_see_history in ["yes", "no", "history"]:
			break
		else:
			print("Type either yes, no or history")

	while True:
		if continue_calculation_or_see_history.lower() == "yes":
			break
		# TODO: After asking for history, I am presented with entering first number.
		#  Ideally I should be asked "Do you want to continue calculation (yes),
		#  leave (no) or see the log (history) of it?" again.
		elif continue_calculation_or_see_history.lower() == "history":
			with open("calculator_history.txt", "r") as calculator_history_file:
				calculator_history = calculator_history_file.readlines()
			for line in calculator_history:
				print(line, end="")
			break
		elif continue_calculation_or_see_history.lower() == "no":
			print("Have a nice day!")
			continue_calculation = "no"
			break

print("Have a nice day!")
