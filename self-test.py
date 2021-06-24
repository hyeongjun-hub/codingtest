# def fuc(arr):
#     num_dic = {}
#     for element in arr:
#         if element in arr[arr.index(element) + 1:]:
#             if element not in num_dic:
#                 num_dic[element] = arr.count(element)
#     if len(num_dic) == 0:
#         print([-1])
#     else:
#         print(list(num_dic.values()))

# def fuc(arr):
#     print(arr.split())



# fuc("12345")
#
# from collections import Counter
#
# c = Counter('abacdfdf')
# d = sorted(c.elements())
# print(d)
# print(c)

data = enumerate([1, 2, 3])
number = [1,2,3]

print(list(map(lambda x: x*2 if x > 2 else 0, number)))

