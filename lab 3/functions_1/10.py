def unique_elements():
    lst_str = input().split()
    lst = []

    for num in lst_str:
        lst.append(int(num))

    unique_lst = []
    
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    
    print(unique_lst)

unique_elements()
