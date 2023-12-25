def check_if_exist(arr):
    s = set()
    for num in arr:
        if num * 2 in s or num / 2 in s:
            return True
        s.add(num)
    return False


arr = [10, 2, 5, 3]
print(check_if_exist(arr))

arr = [3, 1, 7, 11]
print(check_if_exist(arr))
