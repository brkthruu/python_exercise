def lcg(seed, loop, m=2**32, a=214013, c=2531011):
    """Linear congruential generator."""
    for i in range(loop):
        seed = (a * seed + c) % m
        yield seed


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if type(text)!= str:
        print("Text should be string.")
        return 0
    elif option not in ["shuffle", "unique", "ordered", None]:
        print("Invalid Option.")
        return 0

    result = list()
    if option == None:
        result = text.split(sep)
        for i in result:
            yield i

    elif option == "shuffle":
        result = text.split(sep)
        new_result = list()
        for i, j in enumerate(lcg(len(result), len(result))):
            j %= len(result)
            result[i], result[j] = result[j], result[i]
        for i in result:
            yield i

    elif option == "unique":
        for word in text.split(sep):
            if word not in result:
                result.append(word)
        for i in result:
            yield i

    elif option == "ordered":
        result = text.split(sep)
        result.sort(key=str.swapcase)
        for i in result:
            yield i
