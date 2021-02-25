# 78, 65, 89, 86, 55, 91, 64, 89

# find the highest score in class for math subject

all_math_scores = input("Please enter the list of scores:   ").split(',')
high_score = 0
for score in range(0, len(all_math_scores)):
    if int(high_score) < int(all_math_scores[score]):
        high_score = all_math_scores[score]

print(f"The highest score in math = {high_score}")

print(f"The highest score in math = {max(all_math_scores)}")