arr = [1,3,2,4,5,7,6,8]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)