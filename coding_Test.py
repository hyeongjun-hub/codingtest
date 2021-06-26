def solution(v):
    answer = []
    answer1 = []
    answer2 = []
    for i in v:
        answer1.append(i[0])
        answer2.append(i[1])

    for j in answer1:
        newL1 = list(answer1) - answer1[j]
        if j not in newL1:
            answer.append(j)
    for k in answer2:
        newL2 = list(answer2) - answer2[k]
        if k not in newL2:
            answer.append(k)

    return answer