def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
                result += chr((ord(char) - base + direction * shift_amount) % 26 + base)
            elif char.isupper():
                base = ord('A')
                result += chr((ord(char) - base + direction * shift_amount) % 26 + base)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1)

def decrypt(text, shift):
    return caesar_cipher(text, -shift, 1)

# User input
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
choice = input("Choose 'encrypt' or 'decrypt': ").lower()

if choice == 'encrypt':
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
elif choice == 'decrypt':
    decrypted_text = decrypt(text, shift)
    print(f"Decrypted text: {decrypted_text}")
else:
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")