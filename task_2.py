def find_numbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


nums = [12, 345, 2, 6, 7896]
print(find_numbers(nums))

nums = [555, 901, 482, 1771]
print(find_numbers(nums))
