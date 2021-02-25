import random as rand

print("The game of who's gonna pay the bill.")
print("The person whose business card gets picked up is gonna pay the bill.")
print("Now, enter the names")
names = input("Enter the list of names comma separated:  ")

name_list = names.split(",")

if len(name_list) > 1:
    selected_name = rand.randint(0, len(name_list))
    print(f"{name_list[selected_name]} is gonna pay the bill folks")