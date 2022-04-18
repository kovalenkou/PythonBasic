#homework 5 - Find cucumber in the input string
print('Hello! If you want I can find cucumber.')
innput_string = input('Please, input the string with word \"cucumber\" in any place\n')
start_position = innput_string.lower().find('cucumber')
if start_position == -1:
    print('The word \"cucumber\" isn\'t exist in the string. I\'m so sad, that I can\'t find anything else yet')
else:
    print(innput_string[start_position::])
print('Done! Coongrats.')
