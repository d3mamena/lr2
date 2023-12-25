def remove_duplicates(nums):
    if not nums:
        return 0

    unique_count = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_count] = nums[i]
            unique_count += 1

    return unique_count


example_1_nums = [1, 1, 2]
example_1_result = remove_duplicates(example_1_nums)
print(example_1_result, "nums:", example_1_nums[:example_1_result])

example_2_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
example_2_result = remove_duplicates(example_2_nums)
print(example_2_result, "nums:", example_2_nums[:example_2_result])
