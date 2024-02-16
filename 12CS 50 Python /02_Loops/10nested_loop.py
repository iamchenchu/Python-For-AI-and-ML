def main():
    print_square(3)

def print_square(size):
    for i in range(size):          # Outer loop for each row in squeare
        for j in range(size):      # For each brick in a row
            print("#", end="")     # Print the brick
        print()                    # it's below the inner loop and in the outer loop, it goes to the 

main()