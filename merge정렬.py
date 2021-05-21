def merge_sorted(list1, list2):
    i, j = 0, 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
        if i == len(list1):
            return merged_list + list2[j:]
        elif j == len(list2):
            return merged_list + list1[i:]
    return merged_list

def merge(list3):
    lefthalf = list3[:len(list3)//2]
    righthalf = list3[len(list3)//2:]
    if len(list3) < 2:
        return list3
    return merge_sorted(merge(lefthalf),merge(righthalf))



print(merge([1,8,5,4]))