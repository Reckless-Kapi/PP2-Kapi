def histogram():
    lst_str = input().split()
    lst = []

    for num in lst_str:
        lst.append(int(num))

    for num in lst:
        print('*' * num)

histogram()
