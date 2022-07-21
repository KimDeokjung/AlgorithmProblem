# def solution(s, n):
#     answer = ''
#
#     for x in range(len(s)):
#         target = ord(s[x])
#         if target == 32:
#             answer += " "
#             continue
#
#         num = target % 97 if target > 90 else target % 65
#         num += n
#         num %= 26
#         answer += chr(97 + num) if target > 90 else chr(65 + num)
#     return answer

# print(solution(" Abc", 1))


def solution(s):
    num = "0"
    for x in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:s = s.replace(x, num); num = str(int(num) + 1)
    return int(s)

print(solution("23four5six7"))