# 1. Parentheses: Change order of operations
result = (3 + 5) * 2  # (8) * 2 = 16
print(f"Parentheses: (3 + 5) * 2 = {result}")  

# 2. List Indexing and Slicing
my_list = [10, 20, 30, 40, 50]
print(f"Indexing: my_list[2] = {my_list[2]}")  # Get element at index 2 -> 30
print(f"Slicing: my_list[1:4] = {my_list[1:4]}")  # Get elements from index 1 to 3 -> [20, 30, 40]

# 3. Exponentiation (** works right to left)
result = 2 ** (3 ** 2)  # 2 ** 9 = 512
print(f"Exponentiation: 2 ** (3 ** 2) = {result}")

# 4. Unary Operators (+, -, ~)
print(f"Unary -: -5 = {-5}")  
print(f"Unary +: +5 = {+5}")  
print(f"Bitwise NOT: ~5 = {~5}")  # ~5 = -6 (inverts bits)

# 5. Multiplication, Division, Modulo
result = 10 * 2 + 5  # 20 + 5 = 25
print(f"Multiplication + Addition: 10 * 2 + 5 = {result}")

# 6. Addition and Subtraction
result = 10 - 3 + 2  # 7 + 2 = 9
print(f"Addition and Subtraction: 10 - 3 + 2 = {result}")

# 7. Bitwise Shift (<< shifts bits left)
result = 5 << 2  # 5 * 2^2 = 5 * 4 = 20
print(f"Bitwise Shift: 5 << 2 = {result}")

# 8. Bitwise AND, XOR, OR
print(f"Bitwise AND: 5 & 3 = {5 & 3}")  # 5 (101) & 3 (011) = 001 (1)
print(f"Bitwise XOR: 5 ^ 3 = {5 ^ 3}")  # 5 (101) ^ 3 (011) = 110 (6)
print(f"Bitwise OR: 5 | 3 = {5 | 3}")   # 5 (101) | 3 (011) = 111 (7)

# 9. Comparison Operators
result = (10 > 5) == 5  # (True == 5) -> False
print(f"Comparison: 10 > 5 == 5 = {result}")

# 10. Membership and Identity Operators
my_str = "hello"
print(f"Membership: 'h' in my_str = {'h' in my_str}")  # Checks if 'h' is in "hello"
print(f"Identity: 10 is not 5 = {10 is not 5}")  # True since 10 is not 5

# 11. Logical Operators (not, and, or)
result = not False and True  # True
print(f"Logical AND: not False and True = {result}")


 


