def is_prime(number):
    return number > 1 and all(number % i for i in range(2, int(number ** 0.5) + 1))  # True if no divisor found

def get_prime(numbers):
    return [number for number in numbers if is_prime(number)]  # Filter prime numbers

# Print prime numbers from the given list
print(get_prime([2, 3, 4, 5, 10, 13, 17]))  # Output: [2, 3, 5, 13, 17]
