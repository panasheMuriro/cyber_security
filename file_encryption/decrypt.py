from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key

def decrypt_file(file_name):
    # Load the key
    key = load_key()
    cipher = Fernet(key)
    
    # Read the encrypted file data
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Write the decrypted file (removing the `.enc` extension)
    output_file = file_name.replace(".enc", "")
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # Specify the file to decrypt
    file_name = "file_to_encrypt.txt.enc"  # Replace with your target encrypted file
    decrypt_file(file_name)
    print(f"File '{file_name}' has been decrypted!")
