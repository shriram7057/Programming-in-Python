# Creating two tuples
tuple1 = (5, 2, 9, 1)
tuple2 = (8, 3, 7, 4)

# Concatenating the tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Sorting in ascending order
sorted_tuple_asc = tuple(sorted(concatenated_tuple))
print("Sorted Tuple (Ascending):", sorted_tuple_asc)

# Sorting in descending order
sorted_tuple_desc = tuple(sorted(concatenated_tuple, reverse=True))
print("Sorted Tuple (Descending):", sorted_tuple_desc)
