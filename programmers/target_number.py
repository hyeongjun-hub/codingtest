# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

def solution(numbers, target):
    answer = []
    for i in range(len(numbers)):
        if i == 0:
            answer.append(numbers[i])
        else:
            minus = list(answer)
            for j in range(len(answer)):
                answer[j] += numbers[i]
                minus[j] = minus[j] - numbers[i]
            answer += minus
    # 첫 시작이 음수일 때
    answerMinus = []
    for i in range(len(numbers)):
        if i == 0:
            answerMinus.append(-numbers[i])
        else:
            minus = list(answerMinus)
            for j in range(len(answerMinus)):
                answerMinus[j] += numbers[i]
                minus[j] = minus[j] - numbers[i]
            answerMinus += minus
    # 답구하기
    answer += answerMinus
    count = 0
    for i in answer:
        if i == target:
            count += 1
    return count


print(solution([1,1,1,1,1], 3))