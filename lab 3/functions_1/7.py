def has_33():
    nums_str = input().split()
    nums = []

    for num in nums_str:
        nums.append(int(num))

    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print(True)
            return
    print(False)

has_33()
