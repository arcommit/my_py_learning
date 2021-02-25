# Emphasises on the need for multiple if conditions and nested if conditions.

print("Welcome to the rollercoaster ride!!")
print("If you ain't tall, go get a ball!!")

total_amount = 0
height = float(input("Enter your height   "))
if height >= 120:
    print("You can get in for the ride")
    age = int(input("Enter your age   "))
    if age < 12:
        total_amount = 5
    elif 12 < age < 18:
        total_amount = 7
    else:
        total_amount = 12
    photo = input("Do you want a photo of you during the ride? (Y/N):  ")
    if photo == "Y" or photo == "y":
        total_amount = total_amount + 3

    print(f"Please pay: {total_amount}")

else:
    print("Sorry. You can't enter the ride")
