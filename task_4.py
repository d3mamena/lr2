def duplicate_zeros(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1
    return arr


arr = [1, 0, 2, 3, 0, 4, 5, 0]
print(duplicate_zeros(arr))

arr = [1, 2, 3]
print(duplicate_zeros(arr))
