print("Hello! This is a simple calculator.")
continue_calculation = "y"

while continue_calculation.lower() == "y":
	try:
		first_number = float(input("Enter first number: "))
	except ValueError:  # Surround the input statement with a try-except block to catch any ValueError exceptions
		print("Invalid input. Please enter a valid number.")
		continue

	operator = input("+, - , / or *: ")

	# Handling division by zero
	if operator == "/":
		while True:
			# TODO: Don't use try/except for now since we did not learned it yet.
			#  Nevertheless, good solution.
			try:
				second_number = float(input("Enter second number (non-zero): "))
				if second_number == 0:
					print("Error: Division by zero! Please enter a non-zero number.")
					continue
				else:
					break  # Exit the loop if the user enters a non-zero number
			except ValueError:
				print("Invalid input. Please try enter a valid number.")
				continue
	else:
		try:
			second_number = float(input("Enter second number: "))
		except ValueError:
			print("Invalid input. Please try enter a valid number.")
			continue

	if operator == "+":
		# TODO: second_number can be undefined in case "try" block fails.
		operation_result = first_number + second_number
	elif operator == "-":
		operation_result = first_number - second_number
	elif operator == "*":
		operation_result = first_number * second_number
	elif operator == "/":
		operation_result = first_number / second_number
	else:
		print("Invalid operator.")
		continue

		# Check if the result is a whole number
	if operation_result.is_integer():
		operation_result = int(operation_result)

	# Formatting result
	if isinstance(operation_result, float):
		answer = f"{first_number} {operator} {second_number} = {operation_result: .2f}"  # Display with 2 decimal
	else:
		answer = f"{first_number} {operator} {second_number} = {operation_result}"  # As integer if it's a whole number
	print(answer)

	print("Do you want to calculate something else?")
	continue_calculation = input("y/n ")

print("Bye!")
# The "try" block lets you test a block of code for errors.
#
# The "except" block lets you handle the error.
#
# The "else" block lets you execute code when there is no error.
#
# The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
