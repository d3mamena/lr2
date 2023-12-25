def replace_elements(arr):
    max_from_right = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_from_right = max_from_right, max(max_from_right, arr[i])
    return arr


arr = [17, 18, 5, 4, 6, 1]
print(replace_elements(arr))

arr = [400]
print(replace_elements(arr))
