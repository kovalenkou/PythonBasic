# This is my module for sorting functions

def my_bubble_sort(unsorted_list, sort='direct', new_list=True):
    if new_list:
        sorted_list = unsorted_list.copy()
    elif not new_list:
        sorted_list = unsorted_list
    else:
        raise ValueError('Incorrect input for argument \'new_list\'')

    list_len = len(sorted_list)
    if sort.lower() == 'direct':
        while list_len != 0:
            for n in range(0, list_len - 1):
                if sorted_list[n + 1] < sorted_list[n]:
                    sorted_list[n], sorted_list[n + 1] = sorted_list[n + 1], sorted_list[n]
            list_len -= 1
        return sorted_list
    elif sort.lower() == 'reverse':
        while list_len != 0:
            for n in range(0, list_len - 1):
                if sorted_list[n] < sorted_list[n + 1]:
                    sorted_list[n + 1], sorted_list[n] = sorted_list[n], sorted_list[n + 1]
            list_len -= 1
        return sorted_list
    else:
        raise ValueError('Incorrect input for argument \'sort\'')
