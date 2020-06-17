def twoSum(nums, target):
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Args:
        nums (list): List of integers
        target (int):

    Returns:
        list: list containing the two indices of the two numbers that add up to the target
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
