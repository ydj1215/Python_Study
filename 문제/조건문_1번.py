# [1] 세자리 정수를 입력 받은 후, 가장 큰 수 찾기

num = int(input())  # 567
hundred = num // 100  # 5
ten = (num % 100) / 10  # 6
one = num % 10  # 7

list = [hundred, ten, one]
max_number = hundred
for a in list:
    if max_number < a:
        max_number = a

print(max_number)
