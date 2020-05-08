#count.py

import sys

def text_analyzer(str=""):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if str == "":
        print("What is the text to analyze?")
        str = input()
    upletter = 0
    lowletter = 0
    punc = 0
    space = 0
    for i in str:
        if i.isupper():
            upletter+=1
        elif i.islower():
            lowletter+=1
        elif (i >= '!' and i <= '/') or (i >= ':' and i <= '@') or (i >= '[' and i <= '\''):
            punc+=1
        elif i == ' ':
            space+=1
    print("The text contains %d letters:\n" % len(str))
    print("- %d upper letters\n" % upletter)
    print("- %d lower letters\n" % lowletter)
    print("- %d punctuation letters\n" % punc)
    print("- %d spaces" % space)

