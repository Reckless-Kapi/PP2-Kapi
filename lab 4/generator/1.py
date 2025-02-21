def squares(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
list = []

for num in squares(n):
    list.append(num)

print(list)