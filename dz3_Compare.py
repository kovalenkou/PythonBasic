#homework 3 - Compare
print('Hello! No, i\'m not a calculator.\nIf you want I can compare two integer.')
num1 = int(input('Please, input the first integer\n'))
num2 = int(input('Please, input the second integer\n'))
if num1 == num2:
    print('The first integer is equal to the second integer.', num1,  '=', num2)
elif num1 > num2:
    print('The first integer is more than the second integer.', num1,  '>', num2)
else:
    print('The first integer is less than the second integer.', num1,  '<', num2)
print('Done! Coongrats.')
