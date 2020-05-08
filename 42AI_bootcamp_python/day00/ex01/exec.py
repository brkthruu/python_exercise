import sys

args = list(reversed(sys.argv[1:]))

def RevAlpha(arg):
	rev_word = arg[::-1]
	res = ''
	for i in rev_word:
            if i.isupper() or i.islower():
                res += i.swapcase()
            else:
                res += i
	return res
	
result = list()

for arg in args:
	result.append(RevAlpha(arg))
                
print(*result)

