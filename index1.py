import secrets

# Generate two random numbers between 1 and 49
num1 = secrets.randbelow(49) + 1
num2 = secrets.randbelow(49) + 1

# Store the randomly selected numbers in a list
winning_numbers = [num1, num2]

# Ask the user to input their chosen numbers
user_numbers = input("Enter your two numbers separated by a space: ").split()

# Convert the user's numbers to integers
user_numbers = [int(x) for x in user_numbers]

# Check if the user's numbers match the winning numbers
if user_numbers == winning_numbers:
  print("You win the lottery!")
else:
  print("Sorry, you lose.")

import hashlib
import random

# Generate a random seed value
seed = random.getrandbits(256)

# Use a cryptographic hash function to generate the winning numbers
winning_numbers = hashlib.sha256(seed.to_bytes(32, 'big')).hexdigest()

# The resulting hash value is a long string of hexadecimal characters.
# You can use the first two characters of the hash value as the winning numbers
winning_numbers = int(winning_numbers[:2], 16)

# The winning numbers will now be a number between 0 and 99.
# To ensure that the numbers are between 1 and 49, you can use the modulo operator
winning_numbers = winning_numbers % 49 + 1

import random
import secrets

# Generate two random numbers between 1 and 49 using a secure random number generator
winning_numbers = [secrets.randbelow(49) + 1, secrets.randbelow(49) + 1]

# Ask the user to input their chosen numbers
user_numbers = input("Enter your two chosen numbers, separated by a space: ")

# Split the user's input into a list of integers
user_numbers = [int(x) for x in user_numbers.split()]

# Compare the user's numbers to the winning numbers
if user_numbers == winning_numbers:
    print("You won the lottery!")
else:
    print("Sorry, you did not win. The winning numbers were: ", winning_numbers)

# Print the seed value used to generate the winning numbers
print("The seed value used to generate the winning numbers was: ", seed)
