from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for character in original_text:
        if character in alphabet:
            character_position = alphabet.index(character)
            encrypted_text += alphabet[(character_position + shift_amount) % 26]
    return encrypted_text

def decrypt(encoded_text,shift_amount):
    decrypted_text = ""
    for character in encoded_text:
        character_position = alphabet.index(character)
        decrypted_text+=alphabet[(character_position-shift_amount)%26]
    return decrypted_text

def caesarcipher(direction, text, shift):
    if direction == "encode":
        print(f"Here's the encoded result: {encrypt(text,shift)}")
    elif direction == "decode":
        print(f"Here's the decoded result: {decrypt(text,shift)}")
    else:
         print("Invalid choice")

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesarcipher(direction,text,shift)
    doContinue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if doContinue != "yes":
        break