# Treasure Island Game

print("Welcome to Treasure Island. Your mission is to find the treasure")
l_r = input("Which path would you like to take? ""Left"" or ""Right""?  ").lower()

if l_r == 'left':
    s_w = input("Great. You are now at a river. You want to ""swim"" across to the Island or ""wait""? ").lower()
    if s_w == "wait":
        door = input("Great. You reached the Island. "
                     "Now, which door colour would you like to take? "
                     "Red / Yellow / Blue ?").lower()
        if door == "yellow":
            print("Yaay.. You have won yourself a treasure. Congratulations")
        elif door == "blue":
            print("You are gonna watch all the sad movies and die!! no choices")
        elif door == "red":
            print("You get to fight the dragon. sad thing, you die!! no choices")
        else:
            print("You entered a word that does not match the choices. You deserve HELL!!")
    else:
        print("You are attacked by piranha. You die. GAME OVER!!")

else:
    print("You fall into a hole. GAME OVER!!")
