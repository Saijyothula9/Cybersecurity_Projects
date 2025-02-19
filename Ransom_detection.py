import os
import hashlib

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as file:
        sha256.update(file.read())
    return sha256.hexdigest()

# Store hashes before encryption
original_hashes = {file: get_file_hash(file) for file in os.listdir("test_folder")}

# Compare hashes after encryption
for file in os.listdir("test_folder"):
    if original_hashes[file] != get_file_hash(file):
        print(f"File changed: {file} (Potential ransomware activity)")
