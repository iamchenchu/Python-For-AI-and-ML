# used to store sequence of data into one variable 
# it's ordered and unchageble 
# tuples are written using round brackets 

team = ("ram", "chenchu", "bheem", "krishna", "jalaal")
team2=("hari",)
team3 = team + team2
print(team3)
print(team)
print(len(team))
print(team[1])
print(team[-1])
print(team.count("ram"))
print(team.index("bheem"))
print(type(team))
