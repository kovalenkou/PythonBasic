#homework 4 - Calculator 0.2
print('Hello! This is the finest calculator (version 0.2)')
print('This version can plus or minus or multiply or divide two integers')
operation_type = input('Please, choose the type of the operation.\nInput + or - or * or / to continue:\n')
text_input1 = 'Please, input the first integer\n'
text_input2 = 'Please, input the second integer\n'
result = None
if  operation_type == '+':
    num1 = int(input(text_input1))
    num2 = int(input(text_input2))
    result = num1 + num2
    print(num1,  '+', num2, '=', result)
elif operation_type == '-':
    num1 = int(input(text_input1))
    num2 = int(input(text_input2))
    result = num1 - num2
    print(num1,  '-', num2, '=', result)
elif operation_type == '*':
    num1 = int(input(text_input1))
    num2 = int(input(text_input2))
    result = num1 * num2
    print(num1,  '*', num2, '=', result)
elif operation_type == '/':
    num1 = int(input(text_input1))
    num2 = int(input(text_input2))
    if num2 == 0:
        print('Incorect: division by zero')
    else:
        result = num1 / num2
        print(num1,  '/', num2, '=', result)
else:
    print('Incorect input')
print('Done!')
