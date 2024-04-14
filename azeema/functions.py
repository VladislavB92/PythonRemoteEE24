# def - Python inbuilt keyword which means "definition (of a function)"


# Function definition: blueprint / project of a function

# number_1, number_2 - arguments

# (number_1, number_2) in function calling are called parameters

def plus_operation(number_1, number_2):
	return number_1 + number_2


def minus_operation(number_1, number_2):
	return number_1 - number_2


def multiply_operation(number_1, number_2):
	return number_1 * number_2


def division_operation(number_1, number_2):
	if number_2 == 0:
		print("can not divide by zero")
	return number_1 / number_2


# TODO: Indentation are not correct. 4 tabs are required. Fixed.
def process_function(number_1, number_2):
	if plus_operation == "+":
		return plus_operation(number_1 + number_2)

	elif minus_operation == "-":
		return minus_operation(number_1 - number_2)

	elif multiply_operation == "*":
		return multiply_operation(number_1 * number_2)

	elif division_operation == "/":
		return division_operation(number_1 / number_2)

	else:
		return "Error: Invalid operation"

# TODO: Why do you hardcoding numbers? We should ask the user for the input.
result_1 = plus_operation(7, 2)
result_2 = minus_operation(8, 6)
result_3 = multiply_operation(6, 6)
result_4 = division_operation(25, 5)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
