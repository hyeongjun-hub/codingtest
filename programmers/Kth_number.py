def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        sortArray = list()
        i = commands[index][0]
        j = commands[index][1]
        k = commands[index][2]
        sortArray = sorted(array[i - 1:j])
        answer.append(sortArray[k - 1])
    return answer

    # 다른사람의 풀이
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
