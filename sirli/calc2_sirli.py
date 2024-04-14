from calc_functions import calculation

print('Hello, this is a simple calculator!')

while True:
    print('\nWhat would you like to do now?')
    print('Calculate (c), check calculation history (h) or exit (e)?')

    choice = input('Enter your choice (c/h/e): ').lower()

    if choice == 'c':
        while True:
            n_1 = input('Enter first number: ')
            if ',' in n_1:
                print('Please use "." for decimals')
            elif not n_1.replace('.', '', 1).isdigit():
                print('Please enter a valid number')
            else:
                break

        while True:
            operator = input('Enter one of the following: +, -, *, /  ')
            if operator in ['+', '-', '*', '/']:
                break
            else:
                print('Please enter a valid operator')

        while True:
            n_2 = input('Enter second number: ')
            if ',' in n_2:
                print('Please use "." for decimals')
            elif not n_2.replace('.', '', 1).isdigit():
                print('Please enter a valid number')
            else:
                if operator == '/' and float(n_2) == 0:
                    print('You can´t divide by zero. Please enter a valid number')
                else:
                    break

        answer = calculation(n_1, operator, n_2)
        answer = round(answer, 2)
        if answer.is_integer():
            answer = int(answer)
        result = f'{n_1} {operator} {n_2} = {answer}'
        print()
        print(result)

        with open('calc_history.csv', 'a') as calc_history_file:
            calc_history = calc_history_file.write(f'{result}\n')

    elif choice == 'h':
        with open('calc_history.csv', 'r') as calc_history_file:
            calc_history = calc_history_file.readlines()
            for line in calc_history:
                print(line, end='')

    elif choice == 'e':
        print('Bye!')
        break

    else:
        print('Invalid choice. Please enter "c" to calculate, "h" to check history, or "e" to exit.')
