from shift_letters import alphabet
from art import logo
from clear_log import clear

print(logo, end="\n")


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift_amount
                new_char = alphabet[new_position]
                end_text += new_char
            else:
                end_text += char

    elif cipher_direction == "encode":
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
    print(f"\nHere is the {cipher_direction}d result:\n{end_text}", end="\n")


end_cipher = True
while end_cipher:
    direction = input(
        "Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

    stop = input("\nType 'yes' to go again, otherwise 'no':\n").lower()
    if stop == "no":
        end_cipher = False
        print("\n GoodBye!")
    # TODO: clear the log after each encode or decode.
    clear()
    print(logo, end="\n")
