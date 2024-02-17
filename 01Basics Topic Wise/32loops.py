fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for fruit in fruits:
    newlist.append(fruit)

print(newlist)

team = ["ram", "bheem", "bhavyanth", "vinodh", "kalyan", "pandu", "lokesh", "mahesh", "rajini"]
newteam=[]

for member in team:
    if member[0] == 'r':
        newteam.append(member)

print(newteam)


# List comprehension

new_members = [x for x in team if x[0]=="r"]

print(new_members)

titled_team = []

for x in team:
    titled_team.append(x.upper())

print(titled_team)

