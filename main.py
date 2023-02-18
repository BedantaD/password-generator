import random
import string
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Define a function to generate a random password
def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the set of characters
    password = ''.join(random.choice(characters) for i in range(length))

    # Return the generated password
    return password

# Generate a random password with a length of 12 characters
password = generate_password(12)

# Create a file to save the password and date/time information
filename = 'passwords.txt'

# Write the password and date/time information to the file
with open(filename, 'a') as file:
    file.write('Password: ' + password + '\n')
    file.write('Generated on: ' + now.strftime('%Y-%m-%d %H:%M:%S') + '\n\n')

# Print a message to indicate that the password has been saved in the file
print('Your password has been successfully generated. \nRefer to "passwords.txt" to view it.')
