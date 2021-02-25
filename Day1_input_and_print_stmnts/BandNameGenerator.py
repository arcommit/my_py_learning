# to generate a band name based on user inputs.
# ask for the hometown, and user's pet
# get input from user for 2 simple questions.
# combine the two words and print in console as band name.

def question1():
    print("What's the name of your hometown?")
    answer1 = input()
    return answer1


def question2():
    print("Your favorite pet?")
    answer2 = input()
    return answer2


def intro():
    print("Hello")
    name = input("What's your name? \n")
    print(len(name))

intro()
answer1 = question1()
answer2 = question2()

print("Your band name can be:" + answer1 + " " + answer2)
