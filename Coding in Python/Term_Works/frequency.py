def count_with_inbuilt(lst):
    frequency = {}
    for item in lst:
        frequency[item] = lst.count(item)  # Using count() function
    return frequency

def count_without_inbuilt(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1  # First occurrence
    return frequency

# Example usage
numbers = [2, 3, 2, 5, 3, 5, 2, 8, 8, 8, 3]
print("Original list:", numbers)

# Using inbuilt count() function
print("Frequency using count():", count_with_inbuilt(numbers))

# Without using inbuilt count() function
print("Frequency without using count():", count_without_inbuilt(numbers))
