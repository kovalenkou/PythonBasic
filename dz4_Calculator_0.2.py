#homework 4 - Calculator 0.2
print('Hello! This is the finest calculator (version 0.2)')
print('This version can plus or minus or multiply or divide two integers')
operation_type = input('Please, choose the type of the operation.\nInput + or - or * or / to continue:\n')
# check the alloved type of operations
if  operation_type in ('+','-','*','/'):
    num1 = int(input('Please, input the first integer\n'))
    num2 = int(input('Please, input the second integer\n'))
else:
    print('Incorect input the type of the operation!')
# calculate the result
result = None
if  operation_type == '+':
    result = num1 + num2
    print(num1,  '+', num2, '=', result)
elif operation_type == '-':
    result = num1 - num2
    print(num1,  '-', num2, '=', result)
elif operation_type == '*':
    result = num1 * num2
    print(num1,  '*', num2, '=', result)
elif operation_type == '/':
    if num2 == 0:
        print('Incorect: division by zero')
    else:
        result = num1 / num2
        print(num1,  '/', num2, '=', result)
print('Done!')
