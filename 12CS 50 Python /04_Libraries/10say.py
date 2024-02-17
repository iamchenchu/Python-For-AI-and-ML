import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# should run it as on current directory : python3 10say.py Chenchu