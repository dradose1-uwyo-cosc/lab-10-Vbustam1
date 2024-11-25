# Vidal Bustamante
# UWYO COSC 1010
# 11/24/2024
# Lab 10
# Lab Section: 13?
# Sources, people worked with, help given to: NA
# That was a lot easier than I thought it would be. It just worked the first time round.

#import modules you will need 

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

from hashlib import sha256
from pathlib import Path

def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

rockyou_path = Path("/workspaces/lab-10-Vbustam1/rockyou.txt")
hash_path = Path("/workspaces/lab-10-Vbustam1/hash")

try:
    with open(hash_path, 'r') as hash_file:
        target_hash = hash_file.read().strip()
except FileNotFoundError:
    print("Error: Hash file not found.")
    exit(1)
except Exception as e:
    print(f"Error reading hash file: {e}")
    exit(1)

try:
    with open(rockyou_path, 'r', encoding='utf-8', errors='ignore') as rockyou_file:
        for line in rockyou_file:
            password = line.strip()  
            if get_hash(password) == target_hash:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found in the list.")
except FileNotFoundError:
    print("Error: RockYou file not found.")
except Exception as e:
    print(f"Error reading RockYou file: {e}")