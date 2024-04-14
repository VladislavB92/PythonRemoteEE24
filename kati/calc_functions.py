def number_is_digit(test_number):
	# TODO: .isdigit() already returns Boolean True or False.
	#  No need to create a separate function.
	if test_number.replace(".", "", 1).isdigit():
		number_test = "digit"
		return number_test


def plus_operation(first_number, second_number):
	return float(first_number) + float(second_number)


def minus_operation(first_number, second_number):
	return float(first_number) - float(second_number)


def division_operation(first_number, second_number):
	# TODO: This also can be written in one line, just like previous operations.
	second_number = float(first_number) / float(second_number)
	return second_number


def multiplication_operation(first_number, second_number):
	return float(first_number) * float(second_number)


def calculation_operation(first_number, operator, second_number):
	if operator == "+":
		return plus_operation(first_number, second_number)
	elif operator == "-":
		return minus_operation(first_number, second_number)
	elif operator == "*":
		return multiplication_operation(first_number, second_number)
	elif operator == "/":
		return division_operation(first_number, second_number)
	else:
		exit("Time is up ... I have to Exit ...")
