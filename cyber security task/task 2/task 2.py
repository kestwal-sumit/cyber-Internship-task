from PIL import Image
import os

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path).convert('RGB')  # Ensure RGB mode
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )

        encrypted_path = f"encrypted_{os.path.basename(image_path)}"
        img.save(encrypted_path)
        print("🔐 Encrypted image saved as:", encrypted_path)
    except Exception as e:
        print("❌ Encryption failed:", e)

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        decrypted_path = f"decrypted_{os.path.basename(image_path)}"
        img.save(decrypted_path)
        print("🔓 Decrypted image saved as:", decrypted_path)
    except Exception as e:
        print("❌ Decryption failed:", e)

def main():
    print("=== Image Encryption & Decryption Tool ===")
    option = input("Choose (encrypt/decrypt): ").strip().lower()

    if option not in ["encrypt", "decrypt"]:
        print("❌ Invalid option! Please type 'encrypt' or 'decrypt'.")
        return

    image_path = input("Enter image file path: ").strip()

    if not os.path.exists(image_path):
        print("❌ Image file not found.")
        return

    try:
        key = int(input("Enter a numeric key (e.g., 20): "))
    except ValueError:
        print("❌ Key must be an integer.")
        return

    if option == "encrypt":
        encrypt_image(image_path, key)
    else:
        decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
