def numbering(num):
    if num == 'one':
        return '1'
    elif num == 'two':
        return '2'
    elif num == 'three':
        return '3'
    elif num == 'four':
        return '4'
    elif num == 'five':
        return '5'
    elif num == 'six':
        return '6'
    elif num == 'seven':
        return '7'
    elif num == 'eight':
        return '8'
    elif num == 'nine':
        return '9'

def change(string):
    buffer = ''
    num = ''
    for i in origin:
        buffer += i
        if buffer == "one":
            num += numbering(buffer)
            buffer = buffer[3:]
        elif buffer == "two":
            num += numbering(buffer)
            buffer = buffer[3:]
        elif buffer == "three":
            num += numbering(buffer)
            buffer = buffer[5:]
        elif buffer == "four":
            num += numbering(buffer)
            buffer = buffer[4:]
        elif buffer == "five":
            num += numbering(buffer)
            buffer = buffer[4:]
        elif buffer == "six":
            num += numbering(buffer)
            buffer = buffer[3:]
        elif buffer == "seven":
            num += numbering(buffer)
            buffer = buffer[5:]
        elif buffer == "eight":
            num += numbering(buffer)
            buffer = buffer[8:]
        elif buffer == "nine":
            num += numbering(buffer)
            buffer = buffer[4:]
        elif ord(i) > 47 and ord(i) < 56:
            num += i
            buffer = buffer[1:]
    return num

i = 0
while i < 3:
    origin = input("문자열을 입력하시오: ")
    print(change(origin))






