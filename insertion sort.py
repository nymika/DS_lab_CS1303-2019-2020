def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        k = i
        for j in range(i-1,-1,-1):
            if arr[k]<arr[j]:
                arr[j],arr[k] = arr[k],arr[j]
                k-=1
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(*insertion(arr))
