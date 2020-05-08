import sys

num = 0

if len(sys.argv) != 2:
    print('ERROR')
    sys.exit()
elif len(sys.argv) == 2:
    for i in sys.argv[1]:
        if i > '9' or i < '0':
            print ('ERROR')
            sys.exit()

num = int(sys.argv[1])

if num == 0:
    print('I\'m Zero.')
elif num % 2 == 0:
    print('I\'m Even.')
else:
    print('I\'m Odd.')
