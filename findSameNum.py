def find_same_number(some_list):
    result = [0] * len(some_list)
    for i in range(len(some_list)):
        result[some_list[i]] += 1
        if result[some_list[i]] >= 2:
            return some_list[i]

# def find_same_number(some_list):
#     temp_list = list();
#     for value in some_list[:-1]:
#         if value in temp_list:
#             return value
#         else:
#             if value == some_list[-1]:
#                 return value
#             else:
#                 temp_list.append(value)

# 공간복잡도 O(n)미만 사용
# def find_same_number(some_list, start = 1, end = None):
#     if end == None:
#         end = len(some_list) - 1
#
#     # 반복 요소를 찾으면 리턴한다
#     if start == end:
#         return start
#
#     # 중간 지점을 구한다
#     mid = (start + end) // 2
#
#     # 왼쪽 범위의 숫자를 센다. 오른쪽은 리스트 길이에서 왼쪽 길이를 빼면 되기 때문에 세지 않는다
#     left_count = 0
#
#     for element in some_list:
#         if start <= element and element <= mid:
#             left_count += 1
#
#     # 왼쪽과 오른쪽 범위중 과반 수 이상의 숫자가 있는 범위 내에서 탐색을 다시한다
#     if left_count > mid - start + 1:
#         return find_same_number(some_list, start, mid)
#
#     return find_same_number(some_list, mid + 1, end)

# dictionary 이용
# def find_same_number(some_list):
#     dic = {}
#     for item in some_list:
#         if item in dic:
#             return item
#         dic[item] = 1


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
