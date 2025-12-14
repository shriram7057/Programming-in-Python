def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Example usage:
numbers = [10, 23, 45, 70, 11, 15]
result = linear_search(numbers, 70)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
