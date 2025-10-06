# Bitwise Operator Demonstration in Python

# Define variables
x = 10  # Binary: 1010
y = 4   # Binary: 0100

# Perform bitwise operations and display results
print("Bitwise AND (x & y):", x & y)  # AND operation (1010 & 0100 = 0000 -> 0)
print("Bitwise OR (x | y):", x | y)   # OR operation (1010 | 0100 = 1110 -> 14)
print("Bitwise XOR (x ^ y):", x ^ y)  # XOR operation (1010 ^ 0100 = 1110 -> 14)
print("Bitwise NOT (~x):", ~x)       # NOT operation (~1010 = -(1010 + 1) -> -11)
print("Left Shift (x << 2):", x << 2) # Left shift (1010 << 2 = 101000 -> 40)
print("Right Shift (x >> 2):", x >> 2) # Right shift (1010 >> 2 = 0010 -> 2)
