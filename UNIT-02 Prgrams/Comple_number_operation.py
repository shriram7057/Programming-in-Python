def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): return a / b if b != 0 else "Cannot divide by zero"  # Division check

# Taking input for two complex numbers
a = complex(input("Enter First Complex Number: "))
b = complex(input("Enter Second Complex Number: "))

# Displaying menu for operations
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("Choose an option (1-4): "))  # Taking user choice

# Dictionary to map choices to functions
operations = {1: add, 2: sub, 3: mul, 4: div}

# Performing selected operation and printing result
print("Result:", operations.get(choice, lambda x, y: "Invalid choice")(a, b))
