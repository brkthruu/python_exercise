import sys

num = 0

def error_check(str):
    if str[0] == '-':
        for i in str[1:]:
            if i > '9' or i < '0':
                return 0
    else:
        for i in str:
            if i > '9' or i < '0':
                return 0
    return 1

if len(sys.argv) != 2:
    print('ERROR')
    sys.exit()

else:
    if error_check(sys.argv[1]) == 0:
        print ('ERROR')
        sys.exit()

num = int(sys.argv[1])

if num == 0:
    print('I\'m Zero.')
elif num % 2 == 0:
    print('I\'m Even.')
else:
    print('I\'m Odd.')
