def rotateLeft(arr, k):
    
    k = k % len(arr)
    print(f"{k}")
    
    return arr[k:] + arr[:k]


arr = [1, 2, 3, 4, 5]
k = 3

res = rotateLeft(arr, k)

print(res)

