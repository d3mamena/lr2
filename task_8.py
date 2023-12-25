def valid_mountain_array(arr):
    if len(arr) < 3:
        return False

    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i += 1

    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1

    return i == len(arr)


arr = [2, 1]
print(valid_mountain_array(arr))

arr = [3, 5, 5]
print(valid_mountain_array(arr))

arr = [0, 3, 2, 1]
print(valid_mountain_array(arr))
