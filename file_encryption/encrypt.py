from cryptography.fernet import Fernet

# Load or generate the encryption key
def load_key():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_name):
    # Load the key
    key = load_key()
    cipher = Fernet(key)
    
    # Read the file data
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(file_data)
    
    # Write the encrypted file
    with open(f"{file_name}.enc", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    # Specify the file to encrypt
    file_name = "file_to_encrypt.txt"  # Replace with your target file
    encrypt_file(file_name)
    print(f"File '{file_name}' has been encrypted!")
