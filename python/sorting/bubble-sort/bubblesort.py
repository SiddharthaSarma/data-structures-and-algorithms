def bubblesort(nums):
    length = len(nums)
    for i in range(0, length):
        for j in range(0, length - i - 1, 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
