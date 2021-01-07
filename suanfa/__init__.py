def remove_num(nums):
    if len(nums) < 2:
        return len(nums)
    left = 0
    for num in nums:
        if nums[left] != num:
            left += 1
            nums[left] = num
    return left + 1


if __name__ == '__main__':
    nums = [1,1,2,3,3]
    print(remove_num(nums))
