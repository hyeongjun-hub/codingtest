# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
#
# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.

nlist = []

def divisionThree(a):
    n, d = a%3, a//3
    if n == 0:
        n = 4
        d -= 1
    nlist.insert(0, str(n))
    if d <= 0:
        return
    return divisionThree(d)


def solution(n):
    divisionThree(n)
    return "".join(nlist)