#homework 8 - Calculator 0.3
print('Hello! This is the finest calculator (version 0.3)')
print('This version can plus or minus or multiply or divide two integers and more.')
input_msg = 'Please, choose the type of the operation.\nInput \"+\" or \"-\" or \"*\" or \"/\" to operate with two intagers.\n\
If you want to sum more than two intagers please choose \"+++\" operation type.\n'
operation_type = input(input_msg)
result = None
# Check the alloved type of operations (Type \"s\" as start to continue)
if  operation_type in ('+','-','*','/'):
    try:
        num1 = int(input('Please, input the first integer\n'))
        num2 = int(input('Please, input the second integer\n'))
        if  operation_type == '+':
            result = num1 + num2
        elif operation_type == '-':
            result = num1 - num2
        elif operation_type == '*':
            result = num1 * num2
        elif operation_type == '/':
            try:
                result = round(num1/num2, 2)
            except ZeroDivisionError as err:
                print('Incorect input: Result is ♾ !', err)
 #          finally:
 #              print('The end!')
        print('Result is: {1} {0} {2} = {3}'.format(operation_type, num1, num2, result))
    except ValueError as err:
        print('Incorect input: only integers allowed.', err)
#sum more than two integers
elif operation_type == '+++':
    next = True
    result = 0
    print('Please, input an integers to sum or Enter to start operation')
    while next:
        try:
            num = input()
            if num != '':
                result += int(num)
            elif num == '':
                next = False
            else:
                print('Incorect input')
        except ValueError as err:
            print('Incorect input: only integers allowed.', err)
    else:
        print('Total sum:', result)
else:
    print('Incorect input the type of the operation!')
#End of operating
print('Done!')
