# match is simply a switch statement in other languages 

name = input("Please enter your name :")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                     # default case if it's not found the defined cases 
        print("Who are you ?")
