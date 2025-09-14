from getpass import getpass

# Prompt the user to enter their username
username = input('Enter your username: ')

# Securely prompt the user to enter their password without displaying it on the screen
password = getpass('Enter your password: ')
