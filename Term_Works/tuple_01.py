# Creating a tuple that contains other tuples
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (True, False, None))

# Accessing elements from the outer tuple
print("Outer tuple:", nested_tuple)
print("First inner tuple:", nested_tuple[0])
print("Second inner tuple:", nested_tuple[1])
print("Third inner tuple:", nested_tuple[2])

# Accessing elements from inner tuples
print("First element of first tuple:", nested_tuple[0][0])  # 1
print("Second element of second tuple:", nested_tuple[1][1])  # 'b'
print("Third element of third tuple:", nested_tuple[2][2])  # None

# Iterating through outer and inner tuples
print("Iterating through nested tuples:")
for inner_tuple in nested_tuple:
    for item in inner_tuple:
        print(item, end=" ")
    print()  # New line after each inner tuple
