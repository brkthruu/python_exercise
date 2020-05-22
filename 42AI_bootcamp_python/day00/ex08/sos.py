import sys

code = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }


def encodeMorse(data):
    for word in data:
        for i in word:
            if not i.isalpha() and not i.isdigit() and (i != ' '):
                print("ERROR")
                sys.exit()
    result = list()
    for i, word in enumerate(data):
        for letter in word:
            if letter == ' ':
                result.append('/')
            else:
                if letter.islower():
                    letter = letter.upper()
                result.append(code[letter])
            result.append(' ')
        if i != len(data) - 1:
            result.append('/ ')
    return ''.join(result)


result = encodeMorse(sys.argv[1:])
print(result)
