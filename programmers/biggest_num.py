# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers 가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.


def solution(numbers):
    # stringNum = list(map(str, numbers))
    # threeList = list(i for i in stringNum if len(i) == 3)
    # stringNum = list(filter(lambda i: len(i) < 3, stringNum))
    # threeList.sort(key=lambda x: x[2], reverse=True)
    # threeList.sort(key=lambda x: x[1], reverse=True)
    # stringNum += threeList
    # twoList = list(i for i in stringNum if len(i) == 2)
    # stringNum = list(filter(lambda i: len(i) < 2, stringNum))
    # twoList.sort(key=lambda x: x[1], reverse=True)
    # stringNum += twoList
    # stringNum.sort(key=lambda x: x[0], reverse=True)
    # answer = ''
    # for letter in stringNum:
    #     answer += letter
    # return answer

    # 세자리수를 리스트에서 빼고 1과 2의 자리 숫자로 정렬한뒤 리스트에 붙이고
    # 두자리수를 리스트에서 빼고 1의 자리 수로 정렬한뒤 리스트에 붙이고
    # 가장 앞의 수로 비교하여 정렬한 리스트를 반환
    # 하지만 33430이 나오므로 실패(34-3-30이 나와야 함)

    # 문자열을 모두 두번 더 쓴 문자열리스트의 첫째자리 비교를 통해 문제 해결가능
    stringNum = list(map(str, numbers))
    stringNum.sort(key=(lambda x: x*3), reverse=True)
    # answer = ''
    # for letter in stringNum:
    #     answer += letter
    # return answer
    return str(int(''.join(stringNum)))


print(solution([3, 30, 34, 187, 545, 5, 9]))
