def solution(priorities, location):
    # 중복되는 priorities 가 없을 경우 성립
    # answer = []
    # backup = priorities[location]
    # while len(priorities):
    #     if priorities[0] < max(priorities):
    #         priorities.append(priorities.pop(0))
    #     else:
    #         answer.append(priorities.pop(0))
    # return answer.index(backup)+1

    count = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else:
                return count + 1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))

            else:
                priorities.pop(0)
                count += 1
            location -= 1



print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
