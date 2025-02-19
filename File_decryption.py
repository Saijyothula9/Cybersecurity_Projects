import os
from cryptography.fernet import Fernet

# Load the key
with open("ransom_key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Function to decrypt files
def decrypt_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            with open(filepath, "wb") as f:
                f.write(decrypted_data)
            print(f"Decrypted: {filepath}")

decrypt_files("test_folder")  # Decrypts all files in test_folder
print("All files successfully decrypted!")
