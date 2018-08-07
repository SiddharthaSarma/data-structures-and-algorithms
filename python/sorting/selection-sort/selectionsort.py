def selectionsort(nums):
    length = len(nums)
    print(length)
    for i in range(0, length, 1):
        index = i
        for j in range(i, length, 1):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            nums[i], nums[index] = nums[index], nums[i]
            print(nums)

    return nums
