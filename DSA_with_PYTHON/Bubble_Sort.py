arr=[60,50,50,40,30,20,10]
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted Array Using Bubble Sort->",arr)
