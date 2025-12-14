def linear_search(arr, target): 
# arr is the array, n is its size 
    n = len(arr)  
    for i in range(n):      # This loop runs n times in the worst case 
        
        if arr[i] == target:    # One comparison operation     
            return i           # Found                
    return -1               # Not found                  
