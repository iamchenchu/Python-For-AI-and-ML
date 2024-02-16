import sys

if len(sys.argv)< 2:
    sys.exit("Too few arguments")

else:
    for arg in sys.argv:
        print("My name is", arg)

# python3 06loop_sys_exit.py Chenchu reddy
# Note : if we don't start the index from [1:] then the first statement will be printed as My name is 06loop_sys_exit.py
# to avoid that we use slicing of the list 
        
def name():
    if len(sys.argv)< 2:
     sys.exit("Too few arguments")

    else:
        for arg in sys.argv[1:]:
            print("My name is", arg)


name()
# in this above function name() we are ignoring the argv[0] argument so it won't print My name is 06loop_sys_exit.py


