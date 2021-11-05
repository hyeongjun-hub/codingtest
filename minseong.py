# def numbering(num):
#     if num == 'one':
#         return '1'
#     elif num == 'two':
#         return '2'
#     elif num == 'three':
#         return '3'
#     elif num == 'four':
#         return '4'
#     elif num == 'five':
#         return '5'
#     elif num == 'six':
#         return '6'
#     elif num == 'seven':
#         return '7'
#     elif num == 'eight':
#         return '8'
#     elif num == 'nine':
#         return '9'
#
# def change(string):
#     buffer = ''
#     num = ''
#     for i in origin:
#         buffer += i
#         if buffer == "one":
#             num += numbering(buffer)
#             buffer = buffer[3:]
#         elif buffer == "two":
#             num += numbering(buffer)
#             buffer = buffer[3:]
#         elif buffer == "three":
#             num += numbering(buffer)
#             buffer = buffer[5:]
#         elif buffer == "four":
#             num += numbering(buffer)
#             buffer = buffer[4:]
#         elif buffer == "five":
#             num += numbering(buffer)
#             buffer = buffer[4:]
#         elif buffer == "six":
#             num += numbering(buffer)
#             buffer = buffer[3:]
#         elif buffer == "seven":
#             num += numbering(buffer)
#             buffer = buffer[5:]
#         elif buffer == "eight":
#             num += numbering(buffer)
#             buffer = buffer[8:]
#         elif buffer == "nine":
#             num += numbering(buffer)
#             buffer = buffer[4:]
#         elif ord(i) > 47 and ord(i) < 56:
#             num += i
#             buffer = buffer[1:]
#     return num
#
# i = 0
# while i < 3:
#     origin = input("문자열을 입력하시오: ")
#     print(change(origin))

# //// "one4seveneight"    1478
# //// "23four5six7"    234567
# //// "2three45sixseven"    234567
# //// "123"    123



# alpha = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9'
# }
# buffer, result = "", ""
# for letter in "one2two3three4567nine8eight":
#     buffer += letter
#     if buffer in alpha:
#         result += alpha.get(buffer)
#         buffer = ""
#     if buffer.isdigit():
#         result += buffer
#         buffer = ""
# print(result)


def solution(s):
    answer = 0
    a = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
    for i in a:
        s = s.replace(i, str(a.index(i)))
    return int(s)





