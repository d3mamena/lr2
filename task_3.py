def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result


nums = [-4, -1, 0, 3, 10]
print(sorted_squares(nums))

nums = [-7, -3, 2, 3, 11]
print(sorted_squares(nums))
