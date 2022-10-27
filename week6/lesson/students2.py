import csv

name = input("whats your name? ")
home = input("where are you from? ")

with open("students.csv", "a") as file:
# "a" for append mode
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})