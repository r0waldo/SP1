def sorteren():
    list=[4,6,8,2,3,1,5]
    new_list=[]

    while list:
        min = list[0]
        for x in list:
            if x < min:
                min = x
        new_list.append(min)
        list.remove(min)
    print(new_list)
sorteren()
# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function

