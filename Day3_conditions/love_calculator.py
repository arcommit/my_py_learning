print("welcome to love calculator")
name1 = input("What is your name?  ").lower()
name2 = input("What is their name?  ").lower()

sum_true = 0
sum_love = 0
total_name = name1 + name2

sum_true += int(total_name.count('t') + total_name.count('r') + total_name.count('u') + total_name.count('e'))

sum_love += int(total_name.count('l') + total_name.count('o') + total_name.count('v') + total_name.count('e'))

total_sum = int(str(sum_true) + str(sum_love))

# print("T occurs " + str(total_name.count('t')) + " times")
# print("R occurs " + str(total_name.count('r')) + " times")
# print("U occurs " + str(total_name.count('u')) + " times")
# print("E occurs " + str(total_name.count('e')) + " times")
# print("Total = " + str(sum_true))
# print("L occurs " + str(total_name.count('l')) + " times")
# print("O occurs " + str(total_name.count('o')) + " times")
# print("V occurs " + str(total_name.count('v')) + " times")
# print("E occurs " + str(total_name.count('e')) + " times")
# print("Total = " + str(sum_love))

if total_sum < 10 or total_sum > 90:
    print(f"Your score is {total_sum}, you go together like coke and mentos")
elif 40 <= total_sum <= 50:
    print(f"Your score is {total_sum}, you are alright together")
else:
    print(f"Your score is {total_sum}")
