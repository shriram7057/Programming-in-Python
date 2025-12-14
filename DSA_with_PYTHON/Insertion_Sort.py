def insertion_Sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
    #Move element Greater than key one step ahead
        while j>=0 and arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
nums=[90,80,60,50,40,30,20,10]
print(insertion_Sort(nums))
