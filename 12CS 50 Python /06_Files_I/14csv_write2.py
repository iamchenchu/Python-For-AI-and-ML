import csv

name = input("what is your name : ")
home = input("where is your home : ")

with open("students1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # fieldnames=["name", "home"] it indicates the sequence of the name and home 
    writer.writerow({"name":name, "home":home})




