import string
import random

# define a function to generate a random password
def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

# take input for the length of the password
password_length = int(input("Enter the length of the password: "))

# generate a random password
password = generate_password(password_length)

# save the password to a text file
with open("passwords.txt", "a") as file:
    file.write(password + "\n")
    print("Password saved to passwords.txt")
