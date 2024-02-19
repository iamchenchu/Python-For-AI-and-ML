def main():
    x = int(input("What is x :"))
    print("x squared is :", square(x))


def square(n):
    return n+n

if __name__ == "__main__":
    main()



"""
if __name__ == "__main__":
    main()

    The above statement means, the program won't run if it get's imported in someother program, it runs only when ever the it
    runs on it's name on current directory

    It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
"""