def spy_game():
    nums_str = input().split()
    nums = []

    for num in nums_str:
        nums.append(int(num))

    pattern = [0, 0, 7]
    index = 0

    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                print(True)
                return
    print(False)

spy_game()
