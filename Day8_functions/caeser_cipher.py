# build a logic to encrypt and decrypt a message.
# shift all the characters in message based on a certain amount of shift


alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

en_de_code = input("Select your options. 'Encode' or 'Decode' ? ").lower()
if en_de_code == "encode" or en_de_code == "decode":
    message = input("Enter your message here:  ").lower()
    shift = int(input("Enter a shift number:  "))
else:
    print("Invalid format chosen!! Try again.")
    exit()


def encrypt_my_msg():
    encoded_msg = ""
    for letter in message:
        encoded_msg = encoded_msg + letter_shifter(letter)
    print(f"Your encoded message is: {encoded_msg}")


def decrypt_my_msg():
    decoded_msg = ""
    for letter in message:
        decoded_msg = decoded_msg + letter_deshifter(letter)
    print(f"Your decoded message is: {decoded_msg}")


def letter_shifter(letter):
    letter_shifted = ""
    for i in range(0, len(alphabet)):
        if letter == alphabet[i]:
           # print("letter matched")
            if (shift + i + 1) > 26:
               # print(f"total = {shift + i + 1}")
               # print("shift > 26")
                final_number = int(shift + i - 25)
               # print(f"final number = {final_number}")
                letter_shifted = alphabet[final_number - 1]
            else:
                letter_shifted = alphabet[shift + i]
    return letter_shifted


def letter_deshifter(letter):
    letter_shifted = ""
    for i in range(0, len(alphabet)):
        if letter == alphabet[i]:
            print(f"letter matched in {i} position")
            if ((i+2) - shift) <= 0:
                print(f"total = {shift - i}")
                print("shift < 0")
                final_number = int(shift - (i+2) + 25)
                print(f"final number = {final_number}")
                letter_shifted = alphabet[final_number - 1]
            else:
                letter_shifted = alphabet[i - shift]
    return letter_shifted


if en_de_code == "encode":
    encrypt_my_msg()
elif en_de_code == "decode":
    decrypt_my_msg()




