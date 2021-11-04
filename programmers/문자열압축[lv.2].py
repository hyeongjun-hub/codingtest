def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for n in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:n]
        for i in range(n, len(s), n):
            if s[i:i + n] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + n]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)