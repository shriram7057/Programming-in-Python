def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def find_primes(a, b):
    primes = []
    num = a
    while num <= b:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Example usage
a = int(input("Enter the lower bound (a): "))
b = int(input("Enter the upper bound (b): "))
print("Prime numbers between", a, "and", b, "are:", find_primes(a, b))
