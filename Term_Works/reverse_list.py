def reverse_with_reverse_method(lst):
    lst.reverse()
    return lst

def reverse_with_slicing(lst):
    return lst[::-1]

def reverse_with_for_loop(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

# Example usage
original_list = [1, 2, 3, 4, 5]
print("Original list:", original_list)

# Using reverse method
reversed_list1 = reverse_with_reverse_method(original_list.copy())
print("Reversed using reverse():", reversed_list1)

# Using slicing
reversed_list2 = reverse_with_slicing(original_list)
print("Reversed using slicing:", reversed_list2)

# Using for loop
reversed_list3 = reverse_with_for_loop(original_list)
print("Reversed using for loop:", reversed_list3)
