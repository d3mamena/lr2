def sort_array_by_parity(nums):
    even_numbers = [num for num in nums if num % 2 == 0]
    odd_numbers = [num for num in nums if num % 2 != 0]

    return even_numbers + odd_numbers


example_1 = sort_array_by_parity([3, 1, 2, 4])
print(example_1)

example_2 = sort_array_by_parity([0])
print(example_2)
