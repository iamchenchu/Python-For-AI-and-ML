import sys

if len(sys.argv) < 2:
    print("Too few argmuments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, My name is", sys.argv[1])