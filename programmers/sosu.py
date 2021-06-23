# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# numbers 는 길이 1 이상 7 이하인 문자열입니다.
# numbers 는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
from itertools import permutations


def solution(numbers):
    answer = []
    bigList = []
    numList = [i for i in numbers]
    for i in range(1, len(numbers)+1):
        bigList += list(permutations(numList, i))
    intList = [int("".join(j)) for j in bigList]

    for num in intList:
        if num < 2:
            continue
        check = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                check = False
                break
        if check:
            answer.append(num)

    return len(set(answer))


print(solution("17"))
