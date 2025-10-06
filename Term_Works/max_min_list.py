def find_max_min(lst):
    if not lst:
        return None, None  # Handle empty list case
    return max(lst), min(lst)

# Example usage
numbers = [10, 25, 5, 99, 45, 7]
max_num, min_num = find_max_min(numbers)

print("Original list:", numbers)
print("Maximum element:", max_num)
print("Minimum element:", min_num)
