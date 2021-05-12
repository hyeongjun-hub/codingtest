def fuc(arr):
    num_dic = {}
    for element in arr:
        if element in arr[arr.index(element) + 1:]:
            if element not in num_dic:
                num_dic[element] = arr.count(element)
    if len(num_dic) == 0:
        print([-1])
    else:
        print(list(num_dic.values()))


fuc([1, 2, 3, 3, 3, 3, 4, 4])
fuc([3, 2, 4, 4, 2, 5, 2, 5, 5])
fuc([3, 5, 7, 9, 1])
