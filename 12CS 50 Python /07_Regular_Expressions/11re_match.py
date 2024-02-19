import re 
# := walrus operator which means it assign the value and also asks the boolean question if and only if

name = input("What's your name : ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1) 
print(f"Hello, {name}")

