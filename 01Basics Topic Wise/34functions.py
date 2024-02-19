names = ["Ram", "Bheem", "Pandu", "Vijay", "Ajay", "Shammi", "Vinodh", "Vinay", "Hemanth", "Prudhvi", "Govindhi"]
scores = [89, 85, 93, 96, 92, 100, 75, 30, 47, 40, 94]

def make_dict(names, marks):
    sudents_dict = dict(zip(names, marks))
    print(sudents_dict)


make_dict(names, scores)


