import random as rand

print("Lets spin a coin!!!!!")

random_side = rand.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
