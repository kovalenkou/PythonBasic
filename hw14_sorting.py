# homework 14 - Sorting
import random
import my_sort

unsort_list = []
for num in range(9):
    unsort_list.append(random.randint(-100, 100))

sort_type = input('Choose the type of sorting. Press \'D\' for direct or \'R\' for reverse sorting: ')
if sort_type.upper() in ('D', 'R'):
    if sort_type.upper() == 'D':
        sort_type = 'direct'
    else:
        sort_type = 'reverse'
else:
    print('Incorrect input')

new_lst = input('Press \'Y\' to create new list after sorting or \'N\' to sort current list: ')
if new_lst.upper() in ('Y', 'N'):
    if new_lst.upper() == 'Y':
        new_lst = True
    else:
        new_lst = False
else:
    print('Incorrect input')

print(f'This is input list before sorting:\n{unsort_list}')
print('Sorted list:')
print(my_sort.my_bubble_sort(unsort_list, sort_type, new_lst))
print(f'This is input list after sorting:\n{unsort_list}')
