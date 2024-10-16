#! python

import sys

print("Standard Input: ")
argc= len(sys.argv)
#print('There are ' + str(argc) + 'command line arguments')
#sys.argv is a list of CL args stored as strings
for arg in sys.argv:   
    print(arg)
    if arg == '-o': # ALWAYS followed by word
        if ()
    elif arg == '-t': # ALWAYS followed by word
        pass
    elif arg == '-h': # flag, no text
        pass

text = sys.stdin.readline()
lines = []
while text:
    lines.append(text)
    text = sys.stdin.readline()
for line in lines:
    print(line, end='')
