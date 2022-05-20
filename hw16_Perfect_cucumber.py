# homework 16 - Perfect cucumber

def perfect_cucumber():
    p_cucumber = input('You can type right now: ')

    # 3. Чи нема зайвих пробілів у тексті
    assert p_cucumber.replace(' ', '') == p_cucumber, 'Good \'Cucumber\' have not the space characters!'
    assert p_cucumber.isalpha(), 'Good \'Cucumber\' have only alphabets characters!'

    # 2. Чи всі літери, окрім першої, маленькі
    assert p_cucumber[1:].lower() == p_cucumber[1:], 'Your \'Cucumber\' second add next letters isn\'t in lower case!'
    # assert p_cucumber.capitalize() == p_cucumber, 'Your \'Cucumber\' letters aren\'t with lower case!'

    # 1. Слово написано з великої літери
    assert p_cucumber[0].upper() == p_cucumber[0], 'Your \'Cucumber\' isn\'t starts with upper case!'
    # assert p_cucumber.startswith('C'), 'Your \'Cucumber\' starts with lower case!'

    #  4. Чи це саме слово Cucumber, а не щось інше
    assert p_cucumber.lower() == 'cucumber', 'It\'s not the \'Cucumber\'!'

    return p_cucumber


print('I need the Cucumber! Please, type \'Cucumber\' right now.\n'
      'Pay attention, good \'Cucumber\' must be written without mistakes.')
next_step = True
while next_step:
    try:
        text = perfect_cucumber()
        print(text)
        next_step = False
    except AssertionError as error:
        print(error)

print('Done! Thanks')
