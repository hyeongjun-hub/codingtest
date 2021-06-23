def solution(answers):
    answer = []
    count = [0, 0, 0]
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, ans in enumerate(answers):
        if ans == supo1[idx % len(supo1)]:
            count[0] += 1
        if ans == supo2[idx % len(supo2)]:
            count[1] += 1
        if ans == supo3[idx % len(supo3)]:
            count[2] += 1

    for idx, c in enumerate(count):
        if c == max(count):
            answer.append(idx + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))
