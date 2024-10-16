#! python
import sys

# READ FROM STANDARD INPUT
print("Standard Input: ")
#print each line IMMEDIATELY
text = sys.stdin.readline()
while text:
    print(text, end='')
    text = sys.stdin.readline()

# HANDLE ARGS
op1 = ""
op2 = ""
f1, f2, f3 = False, False, False # flags

for i in range(len(sys.argv)):   
    arg = sys.argv[i]
    if arg == '-o': # ALWAYS followed by word
        f1 = True
        op1 = sys.argv[i+1] # store next
    elif arg == '-t': # ALWAYS followed by word
        f2 = True
        op2 = sys.argv[i+1] # store next
    elif arg == '-h': # flag, no text
       f3 = True

print("Command line arguments: ")
if f1:
    print('option 1: ' + op1)
if f2:
    print('option 2: ' + op2)
if f3:
    print('option 3')

#check if i need to handle cases where they're present without values