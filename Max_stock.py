# max_profit은 파라미터로 일별 주식 가격이 들어 있는 리스트
# stock_prices를 받고 최대 수익을 리턴합니다.
# 주식은 딱 한 번만 사고 한 번만 팝니다. 그리고 사는 당일에 팔 수는 없습니다.

def max_profit(stock_list):
    max_check = stock_list[1] - stock_list[0]
    for i in range(1, len(stock_list)):
        minu = min(stock_list[:i])
        maxa = max(stock_list[i:])
        dif = maxa - minu
        if dif > max_check:
            max_check = dif
    return max_check



# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))