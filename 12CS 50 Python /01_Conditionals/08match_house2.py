name = input("Please enter the name :")

match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who are you ?")