def insertionsort(nums):
    length = len(nums)
    for i in range(0, length):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


if __name__ == '__main__':
    print(insertionsort([1, 7, 5, 8, 2, 3, 4]))
