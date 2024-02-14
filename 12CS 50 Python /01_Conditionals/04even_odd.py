x = int(input("Please enter the number : "))

if x % 2 == 0 :
    print(f"{x} is an even number")
else :
    print(f"{x} is an odd number")


def main():
    x = int(input("Please enter the number : "))
    if is_even(x):
        print("Even")
    else :
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()