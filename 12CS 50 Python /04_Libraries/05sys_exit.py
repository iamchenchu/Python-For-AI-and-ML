import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("My name is", sys.argv[1])

# python3 05sys_exit.py Chenchu reddy