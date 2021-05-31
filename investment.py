# 우선 함수 sublist_max는 파라미터로 리스트 profits를 받는데요.
# profits에는 며칠 동안의 수익이 담겨 있습니다.
# 예를 들어서 profits가 [7, -3, 4, -8]이라면 첫 날에는 7달러를 벌었고,
# 둘째 날에는 3달러를 잃었고, 셋째 날에는 4달러를 벌었고, 마지막 날에는 8달러를 잃은 거죠.
# sublist_max 함수는 profits에서 최대 수익을 내는 구간의 수익을 리턴합니다.

def sublist_max(profits):
    temp = list()
    maxi = 0
    for i in range(len(profits)):
        for j in range(i+1):
            if i == 0:
                temp = profits[j:]
            else:
                temp = profits[j:-i]
            if maxi < sum(temp):
                maxi = sum(temp)
    return maxi


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))