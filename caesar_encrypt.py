def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Program ===")
    while True:
        try:
            k = int(input("Enter the key (k): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Change key")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            encrypted = caesar_encrypt(text, k)
            print("Encrypted text:", encrypted)
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            decrypted = caesar_decrypt(text, k)
            print("Decrypted text:", decrypted)
        elif choice == "3":
            try:
                k = int(input("Enter new key (k): "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
