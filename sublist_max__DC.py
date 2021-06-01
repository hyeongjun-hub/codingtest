# sublist_max 함수를 Divide and Conquer 방식으로 풀어볼 텐데요. 시간 복잡도는 O(nlgn)이 되어야 합니다.
# # 이번 sublist_max 함수는 3개의 파라미터를 받습니다.
# # profits: 며칠 동안의 수익이 담겨 있는 리스트
# start: 살펴볼 구간의 시작 인덱스
# end: 살펴볼 구간의 끝 인덱스
# sublist_max는 profits의 start부터 end까지 구간에서 가능한 가장 큰 수익을 리턴합니다.
# # 합병 정렬을 구현할 때 merge_sort 함수를 깔끔하게 작성하기 위해 추가로 merge 함수를 작성했던 것 기억 나시나요?
# 마찬가지로 퀵 정렬을 구현할 때 quicksort 함수에 추가로 partition 함수를 작성했습니다.
# 이번에도 sublist_max 함수에 추가로 새로운 함수를 작성하면 도움이 되실 겁니다.

def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2

    left_sum = 0
    left_max = profits[mid]

    for i in range(mid, start-1, -1):
        left_sum += profits[i]
        left_max = max(left_sum, left_max)

    right_sum = 0
    right_max = profits[mid+1]

    for i in range(mid+1, end+1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max

def sublist_max(profits, start, end):
    mid = (start + end)//2

    if start == end:
        return profits[start]

    left_max = sublist_max(profits, start, mid)
    right_max = sublist_max(profits, mid+1, end)
    mid_max = max_crossing_sum(profits, start, end)

    return max(left_max, right_max, mid_max)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))