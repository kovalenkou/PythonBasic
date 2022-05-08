# homework 9 - Snake
import os
import random
import time

print('Hello! This is the Snake')
print('Now you the Snake will run. Wait for start')
time.sleep(1)
os.system('cls||clear')
print('  |||||  \n'
      ' ||   || \n'
      '     ||  \n'
      '   ||    \n'
      '     ||  \n'
      '||    || \n'
      ' ||||||  \n')
time.sleep(1)
os.system('cls||clear')
print('  |||||  \n'
      ' ||  ||  \n'
      '    ||   \n'
      '   ||    \n'
      ' ||      \n'
      ' ||||||  \n')
time.sleep(1)
os.system('cls||clear')
print('     |   \n'
      '   |||   \n'
      '  | ||   \n'
      '    ||   \n'
      '    ||   \n'
      '  |||||| \n')
time.sleep(1)
os.system('cls||clear')
next_step = True
start_position = 10
while next_step:
    try:
        print(' ' * start_position + '*')
        time.sleep(0.1)
    except KeyboardInterrupt:
        next_step = False
        print(' ' * (start_position - 1) + '0-0')
    start_position += random.randint(-1, 1)
print('Done!')
