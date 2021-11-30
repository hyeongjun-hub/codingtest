import itertools

listA = ['A', 'B', 'C']
permu = itertools.combinations(listA, 2)
print(permu)
permuList = map(''.join, permu)
print(permuList)
listCombine = list(permuList)
print(listCombine)
