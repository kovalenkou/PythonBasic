# homework 11 - Caesar cypher
def caesar_encoder(text, cypher_key):
    """This function encodes the text on Caesar cypher with cypher_key displacement

    :param text: text for encryption
    :param cypher_key: integer for displacement
    :return new_text: text after encryption
    """
    new_text = ''
    for char in text:
        ord_char = ord(char)
        if ord_char in range(65, 91):
            new_ord_char = ord_char + cypher_key
            if new_ord_char > 90:
                new_ord_char = new_ord_char - 90 + 64
            new_text = new_text + chr(new_ord_char)
        elif ord_char in range(97, 123):
            new_ord_char = ord_char + cypher_key
            if new_ord_char > 122:
                new_ord_char = new_ord_char - 122 + 96
            new_text = new_text + chr(new_ord_char)
        else:
            new_text = new_text + chr(ord_char)
    return new_text


def caesar_decoder(text, cypher_key):
    """This function decodes the text on Caesar cypher with cypher_key displacement

    :param text: text for decryption
    :param cypher_key: integer for displacement
    :return new_text: text after decryption
    """
    new_text = ''
    for char in text:
        ord_char = ord(char)
        if ord_char in range(65, 91):
            new_ord_char = ord_char - cypher_key
            if new_ord_char < 65:
                new_ord_char = new_ord_char - 64 + 90
            new_text = new_text + chr(new_ord_char)
        elif ord_char in range(97, 123):
            new_ord_char = ord_char - cypher_key
            if new_ord_char < 97:
                new_ord_char = new_ord_char - 96 + 122
            new_text = new_text + chr(new_ord_char)
        else:
            new_text = new_text + chr(ord_char)
    return new_text


next_step = True
while next_step:
    print('Hello! This is the encoder/decoder for Caesar cypher')
    type_next_step = True
    encoder_decoder_type = None
    while type_next_step:
        encoder_decoder_type = input('Please, input the \'1\' for encryption or \'2\' for decryption: ')
        if encoder_decoder_type in ('1', '2'):
            type_next_step = False
        else:
            print('Incorrect input. Try again')

    input_text = input('Input the text (only alphabet symbols [a-z, A-Z] allowed): ')

    key_next_step = True
    key = None
    while key_next_step:
        try:
            key = int(input('Input the cypher key (only numbers [0-9] allowed): '))
            if 0 <= key <= 9:
                key_next_step = False
            else:
                print('Incorrect input: only integers allowed. Try again')
        except ValueError as err:
            print('Incorrect input: only integers allowed. Try again', err)

    if encoder_decoder_type == '1':
        print(caesar_encoder(input_text, key))
    elif encoder_decoder_type == '2':
        print(caesar_decoder(input_text, key))

    yes_or_no = input('Press \'Y\' to continue or \'N\' to stop: ')
    if yes_or_no.upper() == 'N':
        next_step = False
        print('Thanks for use Caesar cypher encoder/decoder!')
    else:
        print('New round starts!')

print('Done!')
