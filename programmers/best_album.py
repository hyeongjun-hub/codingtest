# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres 와 노래별 재생 횟수를 나타내는 정수 배열 plays 가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres 와 plays 의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
from collections import Counter
import re

def solution(genres, plays):
    index = list(enumerate(plays))
    dic = {}
    all = list(zip(genres, index))
    for i in range(len(all)):
        if all[i][0] in dic.keys():
            dic[all[i][0]] += [all[i][1]]
        else:
            dic[all[i][0]] = [all[i][1]]
    gen = {}
    for k, v in dic.items():
        a = 0
        for i in v:
            a += i[1]
        gen[k] = a
    sgen = sorted(gen.items(), reverse=True)
    answer = []
    for i in range(len(sgen)):
        maxa = 0
        max2 = 0
        for j in range(len(all)):
            if maxa < all[j][1][1] and all[j][0] == sgen[i][0]:
                maxa = all[j][1][1]
        answer.append(maxa)
        for j in range(len(all)):
            if max2 < all[j][1][1] and all[j][0] == sgen[i][0] and max2 < max2:
                max2 = all[j][1][1]
        answer.append(max2)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))