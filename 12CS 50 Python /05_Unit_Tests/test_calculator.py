from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print(" 2 squared was not 4")
    if square(3) != 4:
        print(" 3 squared was not 9")

if __name__ == "__main__":
    main()

# should run this as : python3 test_calculator.py