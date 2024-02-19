import csv

name = input("What is your name : ")
home = input("Where is your home : ")

with open("employees.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
    
