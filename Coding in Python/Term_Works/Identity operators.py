# Identity Operators in Python

a, b = 10, 10
c, d = [1, 2, 3], [1, 2, 3]

print("a is b:", a is b)  # True (same memory)
print("c is d:", c is d)  # False (different objects)
print("a is not b:", a is not b)  # False
print("c is not d:", c is not d)  # True