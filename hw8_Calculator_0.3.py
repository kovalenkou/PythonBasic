#homework 8 - Calculator 0.3
print('Hello! This is the finest calculator (version 0.3)')
print('This version can plus or minus or multiply or divide two integers and more.')
input_msg = 'Please, choose the type of the operation.\nInput \"+\" or \"-\" or \"*\" or \"/\" to operate with two intagers.\n\
If you want to sum more than two intagers please choose \"+++\" operation type.\n'
operation_type = input(input_msg)
result = None
# check the alloved type of operations (Type \"s\" as start to continue)
if  operation_type in ('+','-','*','/'):
    num1 = int(input('Please, input the first integer\n'))
    num2 = int(input('Please, input the second integer\n'))
    if  operation_type == '+':
        result = num1 + num2
        print('Result is: {0} + {1} = {2}'.format(num1, num2, result))
    elif operation_type == '-':
        result = num1 - num2
        print('Result is: {0} - {1} = {2}'.format(num1, num2, result))
    elif operation_type == '*':
        result = num1 * num2
        print('Result is: {0} * {1} = {2}'.format(num1, num2, result))
    elif operation_type == '/':
        if num2 == 0:
            print('Incorect: division by zero')
        else:
            result = num1 / num2
            print('Result is: {0} / {1} = {2}'.format(num1, num2, result))
elif operation_type == '+++':
    next = True
    result = 0
    print('Please, input an integer to sum or Enter to start operation')
    while next:
        num = input()
        if num != '':
            result += int(num)
        elif num == '':
            next = False
        else:
            print('Incorect input')
    else:
        print('Total sum:', result)
else:
    print('Incorect input the type of the operation!')
# calculate the result


print('Done!')
