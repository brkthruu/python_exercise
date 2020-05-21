import sys
import re


def filterwords(argv):
    if len(argv) != 3:
        print("ERROR")
        sys.exit()

    for i in argv[1]:
        if i >= '0' and i <= '9':
            print("ERROR")
            sys.exit()
    for i in argv[2]:
        if i < '0' or i > '9':
            print("ERROR")
            sys.exit()

    strin = argv[1]
    result = []

    for word in strin.split(' '):
        if len(word) > int(argv[2]):
            word = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_\`{|}~\\\\]',
                          '', word)
            result.append(word)
    return result


result = filterwords(sys.argv)
print(result)
