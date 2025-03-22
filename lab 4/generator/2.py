def even(n):
    for i in range(0, n + 1, 2):
        if i == 0 or i == 6 or i == 4 or i==10:
            continue
        yield i

n = int(input())
print(list(even(n)))
