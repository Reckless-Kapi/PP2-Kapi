def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Starting number: "))
b = int(input("Ending number: "))

print(list(squares(a, b)))
