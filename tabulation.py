# 솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다. 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...
#
# 가능한 최대 수익을 리턴시켜 주는 함수 max_profit을 Tabulation 방식으로 작성해 보세요. max_profit은 파라미터 두 개를 받습니다.
#
# price_list: 개수별 가격이 정리되어 있는 리스트
# count: 판매할 새꼼달꼼 개수

def max_profit(price_list, count):
    money_list = price_list
    # 전의 값에서 가장 큰 값 max = money_list[1] + money_list[1]
    # 지금 index의 값(money_list[index])
    i = 2
    while i <= count:
        ma = []
        if i < len(money_list):
            for j in range(i):
                ma.append(money_list[j] + money_list[i - j])
            something = max(ma)
            if money_list[i] < something:
                money_list[i] = something
        else:
            j = 1
            for j in range(1,i-1):
                ma.append(money_list[j] + money_list[i - j])
            something = max(ma)
            money_list.append(something)
        i += 1
    return money_list[count]

    # 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
