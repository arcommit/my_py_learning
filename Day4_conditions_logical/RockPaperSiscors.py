# rock beat scissors
# scissors beat paper
# paper beat rock
# rock = 0, paper = 1, scissors = 2
import random as rand


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("What do you choose? ""0"" for Rock ""1"" for Paper ""2"" for Siscors :  "))
computer_choice = int(rand.randint(0, 2))
print(computer_choice)
if user_choice == computer_choice:
    print("its a draw. Play again!!")
elif user_choice == 0 or user_choice == 1 or user_choice == 2:
    if user_choice == 0:
        print(f"Your choice = \n {rock}")
        if computer_choice == 1:
            print(f"computer choice = \n {paper}")
            print("\nComputer wins. Paper beat Rock!!")
        elif computer_choice == 2:
            print(f"computer choice = \n {scissors}")
            print("\nCongratulations.. You Win.. Rock beat Scissors!!")
    elif user_choice == 1:
        print(f"Your choice = \n {paper}")
        if computer_choice == 2:
            print(f"computer choice = \n {scissors}")
            print("\nComputer wins. Scissors beat paper!!")
        elif computer_choice == 0:
            print(f"computer choice = \n {rock}")
            print("\nCongratulations.. You Win.. Paper beat Rock!!")
    elif user_choice == 2:
        print(f"Your choice = \n {scissors}")
        if computer_choice == 0:
            print(f"computer choice = \n {rock}")
            print("\nComputer wins. Rock beat Scissors!!")
        elif computer_choice == 1:
            print(f"computer choice = \n {paper}")
            print("\nCongratulations.. You Win.. Scissors beat Paper!!")
else:
    print("Invalid Input. You Lost!!!!!")
