nums = [4, 2, 3, 6, 7, 8, 10, 11, 12, 25, 33, 19]


def get_range(nums):
    first_index = 0
    nums.sort()
    values_in_range = []

    def sort_by_range(max_value):
        if first_index == max_value:
            return str(nums[first_index])
        else:
            return str(nums[first_index]) + '-' + str(nums[max_value])

    for char in range(1, len(nums)):
        if nums[char] - nums[char - 1] != 1:
            values_in_range.append(sort_by_range(char - 1))
            first_index = char
    values_in_range.append(sort_by_range(char))
    return values_in_range


stuff = get_range
print(stuff(nums))
