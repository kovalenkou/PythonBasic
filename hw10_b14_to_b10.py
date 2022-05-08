# homework 10 - numeral system: b14 to b10 converter
import math

print('Hello! This is the digits converter from  base 14 numeral system to base 10 numeral system')
# base 14 numeral system literals
base = 14
b14 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13}
print('These are valid characters and their meanings')
for key, value in b14.items():
    print(f'{key} = {value}')

next_step = True
while next_step:
    number = input('Please, input the digit for converting: ').upper()
    converting_number = 0
    count = 0
    for num in number[::-1]:
        converting_number += b14[num.upper()] * math.pow(base, count)
        count += 1
    print(f'You digit \'{number}\' in base 10 numeral system = {int(converting_number)}')
    yes_or_no = input('Press \'Y\' to continue or \'N\' to stop: ')
    if yes_or_no.upper() == 'N':
        next_step = False
        print('Thanks for converting!')
    else:
        print('New round starts!')

print('Done!')
