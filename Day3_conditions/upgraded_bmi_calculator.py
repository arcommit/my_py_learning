# to measure Body mass Index for a person


height = float(input("Enter your height in m  "))
weight = float(input("Enter your wight in kg  "))

bmi = round(weight / (height ** 2))
print("Your bmi is " + str(bmi))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are Overweight")
elif bmi < 35:
    print("You are Obese")
else:
    print("You are clinically obese")