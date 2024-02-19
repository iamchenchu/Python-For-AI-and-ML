def main():
    name = input("What's your name ?")
    print(hello(name))


def hello(to="world"): #if I don't assign any variables then it will put world as the argument
    return f"hello, {to}"


if __name__ == "__main__" :
    main()