# [2] 3개의 정수를 입력 받아 최댓값과 최소값 구하기

a, b, c = map(int, input("3개의 정수를 입력해주세요: ").split())

max_num = a
for i in a, b, c:
    if i > max_num:
        max_num = i

min_num = a
for j in a, b, c:
    if j < min_num:
        min_num = j

print(f"최댓값은 {max_num}이고, 최소값은 {min_num}입니다.")