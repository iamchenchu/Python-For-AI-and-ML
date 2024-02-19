with open("names1.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")

    