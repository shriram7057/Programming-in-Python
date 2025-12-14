customer_ids = [102, 205, 150, 123, 301, 110, 175]

def linear_search(customer_list, target_id):
    for i in range(len(customer_list)):
        if customer_list[i] == target_id:
            return True
    return False

def binary_search(sorted_list, target_id):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target_id:
            return True
        elif sorted_list[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return False

search_id = int(input("Enter Customer ID to search: "))
found_linear = linear_search(customer_ids, search_id)
print("Linear Search: Found" if found_linear else "Linear Search: Not Found")

sorted_ids = sorted(customer_ids)
found_binary = binary_search(sorted_ids, search_id)
print("Binary Search: Found" if found_binary else "Binary Search: Not Found")
