def plus(n_1, n_2):
    return float(n_1) + float(n_2)


def minus(n_1, n_2):
    return float(n_1) - float(n_2)


def multiply(n_1, n_2):
    return float(n_1) * float(n_2)


def divide(n_1, n_2):
    return float(n_1) / float(n_2)


def calculation(n_1, operator, n_2):

    if operator == '+':
        return plus(n_1, n_2)
    elif operator == '-':
        return minus(n_1, n_2)
    elif operator == '*':
        return multiply(n_1, n_2)
    elif operator == '/':
        return divide(n_1, n_2)
    else:
        exit('The Princess is in another castle')
