from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = reduce(lambda x, y: x * y, numbers)
print(result)
