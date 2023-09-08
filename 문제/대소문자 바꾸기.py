# https://www.acmicpc.net/problem/2744
#
# a = input()
#
# new_a = ""  # 변환된 문자열을 저장할 빈 문자열 생성
#
# for i in range(len(a)):
#     if a[i].isupper():
#         new_a += a[i].lower()  # 대문자를 소문자로 변환하여 new_a에 추가
#     else:
#         new_a += a[i].upper()  # 소문자를 대문자로 변환하여 new_a에 추가
#
# print(new_a)  # 변환된 문자열 출력

# for i in input() : # 입력된 input() (문자열) 만큼 순회, Hello → 흠흠흠흠흠
#     print("흠", end="")

result = ""
for e in input(): # aPPle → a순회, P순회, P순회, l순회, e순회
    if e.islower():
        result += e.upper()
    else:
        result += e.lower()
print(result)