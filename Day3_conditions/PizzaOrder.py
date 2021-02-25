#automatic pizza order program
# small pizzas = 15
# medium pizzas = 20
# large pizzas = 25
#additional veggie for small pizza = 2
#additional veggie for medium and large pizza = 3
# extra cheese fro any size = 1

final_bill = 0
print("Welcome to the pizza. Please make your order")
size = input("What is the size of your pizza? S/M/L:  ")
add_veggie = input("Would you like extra veggie on your pizza? Y/N:  ")
extra_cheese = input("Would you like extra cheese on your pizza? Y/N:  ")

if size == 'S':
    final_bill = 15
    if add_veggie == 'Y':
        final_bill += 2
if size == 'M':
    final_bill = 20
    if add_veggie == 'Y':
        final_bill += 3
if size == 'L':
    final_bill = 23
    if add_veggie == 'Y':
        final_bill += 3

if extra_cheese == 'Y':
    final_bill += 2

print(f"You pay: {final_bill} for your pizza")