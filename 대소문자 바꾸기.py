# https://www.acmicpc.net/problem/2744

a = input()
print(len(a))

new_a = ""  # 변환된 문자열을 저장할 빈 문자열 생성

for i in range(len(a)):
    if a[i].isupper():
        new_a += a[i].lower()  # 대문자를 소문자로 변환하여 new_a에 추가
        print(new_a)
    else:
        new_a += a[i].upper()  # 소문자를 대문자로 변환하여 new_a에 추가
        print(new_a)

print(new_a)  # 변환된 문자열 출력
