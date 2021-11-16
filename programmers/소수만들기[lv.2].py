from itertools import combinations as cb


def solution(nums):
    answer = 0
    for a in cb(nums, 3):
        can = sum(a)
        for j in range(2, can):
            if can % j == 0:
                break
        else:
            answer += 1

    return answer
