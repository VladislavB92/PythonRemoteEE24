def plus_operation(first_number, second_number):
	return float(first_number) + float(second_number)


def minus_operation(first_number, second_number):
	return float(first_number) - float(second_number)


def multiplication_operation(first_number, second_number):
	return float(first_number) * float(second_number)


def division_operation(first_number, second_number):
	return float(first_number) / float(second_number)


# TODO: This function is not used at all, delete it.
def calculation(first_number, operator, second_number):
	if operator == '+':
		return plus_operation(first_number, second_number)
	elif operator == '-':
		return minus_operation(first_number, second_number)
	elif operator == '*':
		return multiplication_operation(first_number, second_number)
	elif operator == '/':
		return division_operation(first_number, second_number)
	else:
		exit("Have a nice day!")
