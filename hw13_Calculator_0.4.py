# homework 13 - Calculator 0.4
def digit_validation(number=''):
    """This function validate a digits in the input string

    :param number: count for input digit
    :return: digit
    """
    next_step = True
    while next_step:
        input_digit = input(f'Please, input the {number} digit\n')
        if input_digit == '':
            return input_digit
        else:
            try:
                digit = float(input_digit)
                next_step = False
                if digit.is_integer():
                    return int(digit)
                else:
                    return digit
            except ValueError as val_err:
                print('Incorrect input: only digits allowed.', val_err)


print('Hello! This is the finest calculator (version 0.4)')
print('This version can plus or minus or multiply or divide two digits and validate input for digits.')
input_msg = ('Please, choose the type of the operation. Input \"+\" or \"-\" or \"*\" or \"/\" \
to operate with two digits.\nIf you want to sum more than two digits please choose \"+++\" operation type.\n')
operation_type = input(input_msg)
result = None

# Check the allowed type of operations (Type \"s\" as start to continue)
if operation_type in ('+', '-', '*', '/'):
    num1 = digit_validation('first')
    num2 = digit_validation('second')
    if operation_type == '+':
        result = num1 + num2
    elif operation_type == '-':
        result = num1 - num2
    elif operation_type == '*':
        result = num1 * num2
    elif operation_type == '/':
        try:
            result = round(num1 / num2, 2)
        except ZeroDivisionError as err:
            print('Incorrect input: Result is ♾ !', err)
    print('Result is: {1} {0} {2} = {3}'.format(operation_type, num1, num2, result))

# sum more than two integers
elif operation_type == '+++':
    next_digit = True
    result = 0
    print('Please, input a digits to sum or Enter to start operation')
    while next_digit:
        num = digit_validation()
        if num != '':
            result += num
        elif num == '':
            next_digit = False
        else:
            print('Incorrect input')
    else:
        print('Total sum:', result)
else:
    print('Incorrect input the type of the operation!')
# End of operating
print('Done!')
