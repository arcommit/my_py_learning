# get current age.
# max age = 90
# count the number of days left
# assume 365 days, 52 weeks and 12 months in a year

age = int(input("Please enter your age  "))
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12


print(f"you have {days_left} days, {months_left} months, {weeks_left} weeks left till you reach age of 90")
