#creating functions

def greet():
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today?")

#greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do")
    print("Isn't the weather nice today?")


#greet_with_name("Adam")

def greet_with_name_loc(name, location):
    print(f"Hello {name}")
    print("How do you do")
    print(f"Isn't the {location} weather nice today?")

greet_with_name_loc("Adam","Edinburgh")
