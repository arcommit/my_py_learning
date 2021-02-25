count = 0
for number in range(0, 101):
    if number % 2 == 0:
        count += number

print(count)

count = 0
for number in range(2, 101, 2):
    count += number

print(count)

count = 0
for number in range(1, 101, 2):
    count += number

print(count)