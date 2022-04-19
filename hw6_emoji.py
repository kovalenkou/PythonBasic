#homework 6 - Replace emoji in the input string
print('Hello! If you want I can find a text smiles :), XD, :(, >:(, >:) in the string and replace it to the emoji 🙂, 😂, 🙁, 😠, 😈')
smiles_list = ['>:(','>:)',':)','XD',':(']
emoji_list = ['😠','😈','🙂','😂','🙁']
input_string = input('Please, input the string with text smiles in any place\n')
emoji_index = 0
for smile in smiles_list:
    input_string = input_string.replace(smile, emoji_list[emoji_index])
    emoji_index += 1
print(input_string)
print('Done! Coongrats.')
