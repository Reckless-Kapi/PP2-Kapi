def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
list=[]

for num in even(n):
    list.append(num)
    
print(list)