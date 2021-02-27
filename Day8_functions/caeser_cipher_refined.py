alphabet = "a b c d e f g h i j k l m n o p q r s t u " \
           "v w x y z a b c d e f g h i j k l m n o p " \
           "q r s t u v w x y z".split(" ")
should_continue = True


def caeser(text, shift_number):
    final_text = ""
    if en_de_code == "decode":
        shift_number *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The '{en_de_code}ed' text is = {final_text}")


while should_continue:
    en_de_code = input("Select your options. 'Encode' or 'Decode' ? ").lower()
    message = input("Enter your message here:  ").lower()
    shift = int(input("Enter a shift number:  "))
    shift = shift % 26
    caeser(message, shift)
    try_again = input("You want to try again? Yes/No ? ").lower()
    if try_again == "yes":
        should_continue = True
    else:
        should_continue = False
