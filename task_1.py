def max_ones_in_a_row(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


example_1 = max_ones_in_a_row([1, 1, 0, 1, 1, 1])
example_2 = max_ones_in_a_row([1, 0, 1, 1, 0, 1])

print("Example 1:", example_1)
print("Example 2:", example_2)
