def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()

    if choice not in ["encrypt", "decrypt"]:
        print("Invalid option.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == "encrypt":
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
