def about(func):
    def chenchu():
        print("He is from india")
        func()
        print("He will settle down in india")
    return chenchu

def current():
    print("He is doing his graduation")
    print("He is trying for internships")

# current = about(current)
# current()   

@about
def maybe():
    print("If he don't have option he will settle down outside of india")

maybe()
