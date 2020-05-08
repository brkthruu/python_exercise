import sys

sampleMsg = "Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3"

def check_number(arg):
    if arg[0] == '-':
        arg = arg[1:]
    for i in arg:
        if i < '0' or i > '9':
            return 0

if len(sys.argv) == 1:
    print(sampleMsg)
    sys.exit()
elif len(sys.argv) > 3:
    print('InputError: too many arguments\n')
    print(sampleMsg)
    sys.exit()

for arg in sys.argv[1:]:
    if check_number(arg) == 0:
        print('InputError: only numbers\n')
        print(sampleMsg)
        sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print("{0:<12}".format("Sum:"),num1+num2)
print("{0:<12}".format("Difference:"),num1-num2)
print("{0:<12}".format("Product:"),num1*num2)

try:
    print("{0:<12}".format("Quotient:"),num1/num2)
except ZeroDivisionError:
    print("{0:<12}".format("Quotient:"), "ERROR (div by zero)")

try:
    print("{0:<12}".format("Remainder:"),num1%num2)
except ZeroDivisionError:
    print("{0:<12}".format("Remainder:"), "ERROR (modulo by zero)")
