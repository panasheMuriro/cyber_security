from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

if __name__ == "__main__":
    generate_key()
    print("Encryption key has been generated and saved as 'secret.key'.")
