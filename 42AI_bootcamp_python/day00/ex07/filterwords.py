import sys
import re


def remove_punc(strin, leng):
    result = []

    for word in strin.split(' '):
        if len(word) > int(leng):
            word = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_\`{|}~\\\\]',
                          '', word)
            result.append(word)
    return result


def filterwords(argv):
    if len(argv) != 3:
        print("ERROR")
        sys.exit()
    for i in argv[1]:
        if i.isdigit():
            print("ERROR")
            sys.exit()
    for i in argv[2]:
        if not i.isdigit():
            print("ERROR")
            sys.exit()

    strin = argv[1]
    leng = argv[2]

    result = remove_punc(strin, leng)

    return result


result = filterwords(sys.argv)
print(result)
