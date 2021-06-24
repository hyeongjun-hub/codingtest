# 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중,
# 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다
#
# 삼각형의 높이는 1 이상 500 이하입니다.
# 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i - 1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1:j+1])
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))