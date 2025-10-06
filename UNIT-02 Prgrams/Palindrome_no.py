def is_palindrome(number):
    number_string = str(number)  # Convert number to string
    return number_string == number_string[::-1]  # Check if it reads the same backward

# Example usage
number = 121
print(is_palindrome(number))  # Output: True or False
