# homework 12 - Counts the chars in the input string
def chars_count(input_string):
    """This function counts the chars in the input string

    :param input_string: input string
    :return: dict {char1:count, char2:count, ...}
    """
    chars = dict()

    for input_char in input_string:
        if input_char in chars:
            chars[input_char] += 1
        else:
            chars[input_char] = 1
    return chars


print('Hello! If you want I can count a chars in the input string')
chars_in_line = chars_count(input('Please, input a text in the input line.\n'))

print('Input string contains:')
for char_item, count_item in chars_in_line.items():
    print(f'\"{char_item}\" finds \"{count_item}\" times')
print('Done!')
