def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
list = []

for num in countdown(n):
    list.append(num)

print(list)