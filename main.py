# Caesar Cipher
# Here we will encode or decode the message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(user_input, text, shift):
    plain_text = ""
    if user_input == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            index_no = alphabet.index(char)
            new_position = index_no + shift
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The {user_input}d text is {plain_text}")


should_continue = True

while should_continue:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Shift number should be in range of 0-25
    shift = shift % 25
    caesar(user_input=user_input, text=text, shift=shift)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == 'no':
        should_continue = False
